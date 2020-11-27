from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image


# TODO: this should probably live in a file/module on its own
def center_and_crop_image(img):
    dim = min(img.width, img.height)
    left = (img.width - dim) // 2
    top = (img.height - dim) // 2
    right = (img.width + dim) // 2
    bottom = (img.height + dim) // 2
    return img.crop((left, top, right, bottom))


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    slug = models.SlugField(null=False, unique=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    display_name = models.CharField(max_length=64)
    bio = models.TextField(max_length=256, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"
    
    # TODO: set this up to use the local filesystem in DEBUG? LOCAL? mode
    # TODO: See AWS Lambda
    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)

    #     # resize image (you can make this more efficient)
    #     img = Image.open(self.image.path)
    #     img = center_and_crop_image(img)
    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)
    
    def get_absolute_url(self):
        return reverse('profile-detail', kwargs={'slug': self.slug})