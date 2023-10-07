from django.db import models
from django.utils.text import slugify
from django_resized import ResizedImageField
# Create your models here.



class Project(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    client = models.CharField(max_length=150)
    description = models.TextField()
    image = ResizedImageField(size=[2000, 1600],quality=100, upload_to='project')
    image2 = ResizedImageField(size=[2000, 1600],quality=100, upload_to='project')
    image3 = ResizedImageField(size=[2000, 1600],quality=100, upload_to='project')
    image4 = ResizedImageField(size=[2000, 1600],quality=100, upload_to='project', blank = True, null = True, default='media/c.jpg')
    image5 = ResizedImageField(size=[2000, 1600],quality=100, upload_to='project', blank = True, null = True, default='media/c.jpg')
    image6 = ResizedImageField(size=[2000, 1600],quality=100, upload_to='project', blank = True, null = True, default='media/c.jpg')
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
    currency = models.CharField(max_length=70)
    budget = models.PositiveIntegerField()
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