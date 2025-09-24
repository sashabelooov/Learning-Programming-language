from django.db import models


class Language(models.Model):
    name = models.CharField(max_length=50)  # Python, C++, Java, React
    slug = models.SlugField(unique=True)
    image = models.ImageField(
        upload_to='language_images/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name


class Topic(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='topics')
    title = models.CharField(max_length=200)
    order = models.PositiveIntegerField(editable=False)  # qoʻlda emas, avtomatik

    def save(self, *args, **kwargs):
        if self._state.adding and self.order is None:  # yangi yaratilsa
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
    order = models.PositiveIntegerField(editable=False)  # avtomatik

    def save(self, *args, **kwargs):
        if self._state.adding and self.order is None:
            last_order = Content.objects.filter(topic=self.topic).aggregate(
                models.Max("order")
            )["order__max"]
            self.order = (last_order or 0) + 1
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Content {self.order} for {self.topic.title}"
