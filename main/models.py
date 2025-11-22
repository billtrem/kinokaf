from django.db import models

class LandingAsset(models.Model):
    title = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="landing/")

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title or f"Landing Asset {self.id}"
