from django.db import models
from django.utils.text import slugify
from django_resized import ResizedImageField
# Create your models here.


class Member(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=70)
    image = ResizedImageField(size=[385, 300],quality=100, crop=['middle', 'center'], upload_to='profile')
    
class Project(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    client = models.CharField(max_length=150)
    description = models.TextField()
    image = ResizedImageField(size=[400, 300], quality=100, crop=['middle', 'center'], upload_to='project')
    image2 = ResizedImageField(size=[400, 300], quality=100, crop=['middle', 'center'], upload_to='project')
    image3 = ResizedImageField(size=[400, 300],quality=100, crop=['middle', 'center'], upload_to='project')
    slug = models.SlugField(null=True, blank=True)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-date']

class Contact(models.Model):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    email = models.EmailField(max_length=254)
    phone = models.BigIntegerField()
    message = models.TextField()

class Service(models.Model):
    flaticon_promotion = "flaticon-promotion"
    flaticon_web_programming = "flaticon-web-programming"
    flaticon_creativity = "flaticon-creativity"

    category_choices = [(flaticon_promotion,"flaticon-promotion" ), (flaticon_web_programming, "flaticon-web-programming"), (flaticon_creativity, "flaticon-creativity" )
    ]

    name = models.CharField(max_length=70)
    description = models.TextField()
    image = ResizedImageField(size=[385, 241],quality=100, crop=['middle', 'center'], upload_to='service')
    question1 = models.TextField()
    answer1 = models.TextField()
    question2 = models.TextField()
    answer2 = models.TextField()
    question3 = models.TextField()
    answer3 = models.TextField()
    question4 = models.TextField()
    answer4 = models.TextField()
    icon =models.CharField(max_length=50, choices=category_choices)
    slug = models.SlugField(null=True, blank=True)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)