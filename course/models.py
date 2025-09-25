from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

class Language(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='language_images/', blank=True, null=True)

    def __str__(self):
        return self.name

class Topic(models.Model):
    language = models.ForeignKey("Language", on_delete=models.CASCADE, related_name="topics")
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    order = models.PositiveIntegerField(editable=False, null=True, blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='subtopics')

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while Topic.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug

        if self._state.adding and self.order is None:
            last_order = Topic.objects.filter(language=self.language).aggregate(
                models.Max("order")
            )["order__max"]
            self.order = (last_order or 0) + 1

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.language.name} - {self.title}"

class Content(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='contents')
    text = models.TextField()
    link = models.URLField(blank=True, null=True)
    code = models.TextField(blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)
    order = models.PositiveIntegerField(editable=False)

    def save(self, *args, **kwargs):
        if self._state.adding and self.order is None:
            last_order = Content.objects.filter(topic=self.topic).aggregate(
                models.Max("order")
            )["order__max"]
            self.order = (last_order or 0) + 1
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Content {self.order} for {self.topic.title}"



class Comment(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=50, blank=True)  # anonymous uchun
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Comment by {self.user.username} on {self.content}"



class Rating(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 6)])
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('content', 'user')
    
    def __str__(self):
        return f"Rating {self.rating} by {self.user.username} on {self.content}"