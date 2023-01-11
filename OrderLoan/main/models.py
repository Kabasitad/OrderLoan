from django.db import models

# Create your models here.
class Loan_order(models.Model):
	Firstname = models.CharField(max_length=200)
	Lastname = models.CharField(max_length=200)
	Loan = models.IntegerField()


	def __str__(self):
		return self.Firstname , self.Lastname