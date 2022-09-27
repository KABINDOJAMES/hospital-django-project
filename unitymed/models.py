from django.db import models
from django.urls import reverse

# Create your models here.


class Service(models.Model):
    title = models.CharField(max_length=70, unique=True)
    slug = models.CharField(max_length=80, unique=True)
    body = models.TextField(max_length=10000)
    keywords = models.TextField(max_length=100)
    description = models.TextField(max_length=100)
    image = models.ImageField(null=True, blank=True, upload_to="media/")
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('service-detail', args=[str(self.slug)])
    
    class Meta:
        ordering = ['-date']

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        def __str__(self):
            return self.subject
