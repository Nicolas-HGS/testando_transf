from django.db import models


class Topic(models.Model):
    texto = models.TextField()
    nome = models.CharField(max_length=255, null=True)
    data = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'core'
