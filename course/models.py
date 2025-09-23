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
    order = models.PositiveIntegerField(default=0)  # tartibni saqlash uchun

    def __str__(self):
        return f"{self.language.name} - {self.title}"


class Content(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='contents')
    text = models.TextField()          # lesson matni + misollar
    link = models.URLField(blank=True, null=True)
    code = models.TextField(blank=True, null=True)  # code snippet
    video_url = models.URLField(blank=True, null=True)  # video link
    order = models.PositiveIntegerField(default=0)  # topic ichidagi content tartibi

    def __str__(self):
        return f"Content {self.order} for {self.topic.title}"
