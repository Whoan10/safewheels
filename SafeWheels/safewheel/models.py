from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User

class Estabelecimentos(models.Model):
    nome = models.ForeignKey(User, on_delete=models.CASCADE)
    nomeE = models.CharField(max_length=100)
    local = models.CharField(max_length=100)
    desc = models.CharField(max_length=255, blank=True, null=True)
    imagens = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return self.nomeE