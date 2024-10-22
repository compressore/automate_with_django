from django.db import models

class Student(models.Model):
  roll_no = models.CharField(max_length=10)
  name = models.CharField(max_length=255)
  age = models.IntegerField()

  def __str__(self):
    return self.name


class Customer(models.Model):
  name = models.CharField(max_length=255)
  email = models.EmailField()
  phone = models.CharField(max_length=12)

  def __str__(self):
    return self.name