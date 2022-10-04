from django.db import models


class Image (models.Model):
    image = models.FileField()

    def __str__(self):
        return str(self.image.name)
