from typing import Iterable, Optional
from django.db import models

from .services import (
    upload_sertificate_path, upload_coding_lang_path,
    upload_quote_path, upload_cv_path, upload_avatar_path,
    upload_client_logo_path
)

class About(models.Model):
    photo = models.ImageField(upload_to=upload_avatar_path)
    cv = models.FileField(upload_to=upload_cv_path, blank=True, null=True)
    about_me = models.CharField(max_length=350, blank=True)

    def save(self, *args, **kwargs):
        if About.objects.exists() and not self.pk:
            pass
        else:   
            return super(About, self).save(*args, **kwargs)


class Summary(models.Model):
    theme = models.CharField(max_length=50)
    body = models.CharField(max_length=350)
    icon = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.theme
    

class Quote(models.Model):
    author = models.CharField(max_length=100)
    body = models.CharField(max_length=300)
    from_where = models.CharField(max_length=100)
    image = models.ImageField(upload_to=upload_quote_path)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} -> {self.from_where}"
    

class Client(models.Model):
    name = models.CharField(max_length=30)
    logo = models.ImageField(upload_to=upload_client_logo_path)

    def __str__(self) -> str:
        return self.name


class FunFact(models.Model):
    projects = models.PositiveSmallIntegerField(default=1)
    clients = models.PositiveSmallIntegerField(default=1)
    work_hour = models.PositiveSmallIntegerField(default=0)
    posts = models.PositiveSmallIntegerField(default=0)

    def save(self, *args, **kwargs):
        if FunFact.objects.exists() and not self.pk:
            raise ValueError("You can add only one item for this model")
        else:
            super(FunFact, self).save(*args, **kwargs)
            

class SocialNetwork(models.Model):
    name = models.CharField(max_length=50, unique=True)
    url = models.URLField(max_length=200)
    is_active = models.BooleanField(default=True)
    order = models.PositiveSmallIntegerField(default=0, blank=True, null=True)

    class Meta:
        ordering = ['order',]

    def __str__(self):
        return self.name
    

class Education(models.Model):
    edu_name = models.CharField(max_length=250, unique=True) 
    year = models.CharField(max_length=50) 
    specialty = models.CharField(max_length=50)
    about = models.CharField(max_length=50)

    def __str__(self):
        return self.edu_name
    

class Experience(models.Model):
    company = models.CharField(max_length=250, unique=True) 
    year = models.CharField(max_length=50) 
    specialty = models.CharField(max_length=50)
    about = models.CharField(max_length=500)

    def __str__(self):
        return self.company
    

class Sertificate(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=50)
    logo = models.ImageField(upload_to=upload_sertificate_path)
    image = models.ImageField(upload_to=upload_sertificate_path)
    year = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    order = models.PositiveSmallIntegerField(blank=True, null=True)

    class Meta:
        ordering = ['order',]

    def __str__(self):
        return self.name
    

class CodingLanguage(models.Model):
    name = models.CharField(max_length=30)
    logo = models.ImageField(upload_to=upload_coding_lang_path)
    is_active = models.BooleanField(default=True)
    order = models.PositiveSmallIntegerField(blank=True, null=True)

    class Meta:
        ordering = ['order',]

    def __str__(self):
        return self.name





class Contact(models.Model):
    tel = models.CharField(max_length=20, blank=True)
    tel1 = models.CharField(max_length=20, blank=True)
    city = models.CharField(max_length=50, blank=True)
    region = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=50, blank=True)

    def __str__(self):
        return self.tel
    
    def save(self, *args, **kwargs):
        if Contact.objects.exists() and not self.pk:
            pass
        else:   
            return super(Contact, self).save(*args, **kwargs)
    

class UserLetter(models.Model):
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=14)
    subject = models.CharField(max_length=100)
    body = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.full_name} -> {self.subject}"
    
