from django import forms
from django.utils import timezone

class ContactForm(forms.Form):
	name = forms.CharField(max_length=40)
	email = forms.EmailField(max_length=254)
	add = forms.CharField(max_length=40)
	# text = forms.TextField()
	# date = timezone.now