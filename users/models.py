from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from .image_utils import CenterAndCrop


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    slug = models.SlugField(null=False, unique=True)
    image = ProcessedImageField(default='default.jpg',
                                       upload_to='profile_pics',
                                       processors=[CenterAndCrop(), ResizeToFill(300, 300)])
    display_name = models.CharField(max_length=64)
    bio = models.TextField(max_length=256, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"
    
    def get_absolute_url(self):
        return reverse('profile-detail', kwargs={'slug': self.slug})