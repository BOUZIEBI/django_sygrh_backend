from django.db import models



class Article(models.Model):
    titre = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    date_publication = models.DateTimeField(auto_now_add=True)
    est_actif = models.BooleanField(default=True)

    class Meta:
        ordering = ["-date_publication"]

    def __str__(self) -> str:
        return self.titre

# Create your models here.
