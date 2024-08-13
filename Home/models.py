from django.db import models

#make a plan for your models in a book,
#stop your server from running.
#when defining the models be restrict "don't trust the users" .
#put restrictions so that you get clear data.
#make sure you use strict datatypes
#make your migrations first after creating  your models such that django can convert your model into sql object , 
#this is done in the background.this is done to prepare yo models
#then migrate to move it to the database
#during the preparation and moving , make sure your server is not runnning.
#then you can start your server.

# Create your models here.
#you can create many models 
class Student(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()


class Test_list(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    message = models.CharField(max_length=512)
    date = models.DateTimeField()


class Todo_list(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateTimeField()
    description = models.CharField(max_length=512)
    label = models.CharField(max_length=255)
        