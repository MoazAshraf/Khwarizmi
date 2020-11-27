from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.template.defaultfilters import slugify


class Algorithm(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(null=False, unique=True)
    description = models.TextField(blank=True)
    code = models.TextField(blank=True)
    date_created = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    # this function is used to locate a specific instance of the model
    # e.g. the AlgorithmCreateView uses it to redirect the user to the
    # algorithm's page after the algorithm has been created. 
    def get_absolute_url(self):
        return reverse('algorithm-detail', kwargs={'slug': self.slug})
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class Comment(models.Model):
    content = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    algorithm = models.ForeignKey(Algorithm, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.author.username}'s comment on \"{self.algorithm.title}\""
    
    def get_absolute_url(self):
        return reverse('algorithm-detail', kwargs={'slug': self.algorithm.slug})