from django.db import models
from django.urls import reverse

# Create your models here.


class Service(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.CharField(max_length=150, unique=True)
    body = models.TextField(max_length=10000)
    keywords = models.TextField(max_length=1000)
    description = models.TextField(max_length=1000)
    image = models.ImageField(null=True, blank=True, upload_to="media/")
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('service-detail', args=[str(self.slug)])
    
    class Meta:
        ordering = ['-date']

class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    subject = models.CharField(max_length=150)
    message = models.TextField(max_length=2000)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        def __str__(self):
            return self.subject

class Pharmacy(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField(max_length=5000)
    date = models.DateTimeField(auto_now_add=True)
    image_url = models.TextField(blank=True)
    image = models.ImageField(upload_to='media/', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Pharmacy'

    def __str__(self):
        return self.title

class SocialMediaLinks(models.Model):
    title = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now_add=True)
    link = models.CharField(max_length=3000)
    image_url = models.TextField(blank=True)
    alt = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Socila Media Links'

    def __str__(self):
        return self.title

class Home(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField(blank=True)
    image_url = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='media/', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Home'

    def __str__(self):
        return self.title

class AboutUs(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'About Us'

    def __str__(self):
        return self.title


