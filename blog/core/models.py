from django.db import models

class Post(models.Model):
    name = models.CharField(max_length=255)
    data = models.TextField()
    malumot = models.TextField()
    tanlov = models.CharField(max_length=20)
    imgs = models.CharField(max_length=255)
    imge = models.CharField(max_length=255)
    img = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name
