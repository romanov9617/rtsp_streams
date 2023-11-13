from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your models here.



class Video(models.Model):
    rtsp_link = models.CharField(verbose_name="Ссылка на видео-поток")
    camera_name = models.CharField(verbose_name="Название камеры")
    address = models.CharField(blank=True, verbose_name="Адрес")
    is_public = models.BooleanField(default=False, verbose_name="Публичный")
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, related_name="videos", default=None, verbose_name="Автор")


    def __str__(self) -> str:
        return self.camera_name

    def get_absolute_url(self):
        return reverse('video_stream', kwargs={'video_id': self.id})




