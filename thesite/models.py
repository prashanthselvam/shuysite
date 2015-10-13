from django.db import models
from django.utils import timezone

class Message(models.Model):
	name = models.CharField(max_length=40)
	email = models.EmailField()
	subject = models.CharField(max_length=200)
	text = models.TextField()
	message_date = models.DateTimeField(
            default=timezone.now)

	def __str__(self):
		return self.name