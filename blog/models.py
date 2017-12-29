from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField("Заголовок", max_length=200)
    text = models.TextField("Текст")
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(
            blank=True, null=True)
    image = models.ImageField(upload_to='images', blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.pk)])

    class Meta:
        ordering = ["-published_date"]
