from django.db import models
from django.contrib.auth.models import User
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
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f"{self.user.username} Profile"
    
    def save(self):
        super().save()

        # resize image (you can make this more efficiently)
        img = Image.open(self.image.path)
        img = center_and_crop_image(img)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)