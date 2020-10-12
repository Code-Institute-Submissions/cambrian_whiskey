from django.db import models
# from django import ModelForm
# from django import forms

# Create your models here.

class Contact(models.Model):
  name = models.CharField(max_length=30, blank=False)
  email_address = models.CharField(max_length=30, blank=False)
  subject = models.CharField(max_length=60, blank=False)
  message = models.TextField(blank=False)

  def __str__(self):
    return self.name

