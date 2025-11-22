from django.db import models
from cloudinary.models import CloudinaryField

class LandingAsset(models.Model):
    title = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)

    # ⬇️ This forces Cloudinary upload (fixes your problem)
    image = CloudinaryField("image", blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title or f"Landing Asset {self.id}"
