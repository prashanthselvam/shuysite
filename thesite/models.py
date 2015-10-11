from django.db import models
from django.utils import timezone

class Message(models.Model):
	name = models.CharField(max_length=40)
	email = models.EmailField(max_length=254)
	text = models.TextField()
	date = models.DateTimeField(
		default=timezone.now)