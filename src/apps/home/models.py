from django.db import models

# Create your models here.

class Bussiness(models.Model):
	name = models.CharField(max_length=64)
	def __str__(self):
		return self.name
	def get_bussiness(self):
		return self

class Student(models.Model):
	name = models.CharField(max_length=64)
	alias = models.CharField(max_length=64,unique=True)
	mark = models.DecimalField(max_digits=4, decimal_places=2)
	bussiness = models.ForeignKey(Bussiness)
	def __str__(self):
		return self.alias
