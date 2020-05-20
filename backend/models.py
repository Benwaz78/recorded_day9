from django.db import models
from backend.options import REFERER_FIELD, GENDER_FIELD, CHOOSE

# Create your models here.

class ContactModel(models.Model):
	name = models.CharField(max_length=120)
	subject = models.CharField(max_length=120)
	email = models.EmailField()
	gender = models.CharField(max_length=15, choices=GENDER_FIELD)
	referer = models.CharField(max_length=30, choices=REFERER_FIELD, default=CHOOSE, null=True, blank=True)
	message = models.TextField(null=True, blank=True)

	def __str__(self):
		return self.name

