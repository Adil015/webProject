from django.db import models

# Create your models here.
class Contact(models.Model):
    comment = models.TextField()
    email = models.CharField(max_length=122)
    
    def __str__(self):
        return self.email
class Intro(models.Model):
    Intro_Name = models.CharField( max_length=100)
    Intro_Status = models.CharField( max_length=100)
    Intro_par = models.TextField()
    image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    
    def __str__(self):
        return self.Intro_Name

class Edu(models.Model):
    institute = models.CharField(max_length=200)
    degree = models.CharField(max_length=100)
    year = models.CharField(max_length=50)

    def __str__(self):
        return self.institute

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technologies = models.CharField(max_length=200)

    def __str__(self):
        return self.title
    
class Skill(models.Model):
    pic = models.ImageField(upload_to='c++.png/', null=True, blank=True)
    name = models.CharField(max_length=100)
    info = models.CharField(max_length=100)
    desc_1 = models.CharField(max_length=100)
    desc_2 = models.CharField(max_length=100)
    desc_3 = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Exp(models.Model):
    desc = models.TextField()
    