from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm


# Create your views here.

def home(request):
    return render(request, 'thesite/home.html', {})

def fine_art(request):
	return render(request, 'thesite/fine_art.html', {})

def about(request):
	return render(request, 'thesite/about.html', {})

def graphic_design(request):
	return render(request, 'thesite/graphic_design.html', {})

def video(request):
	return render(request, 'thesite/video.html', {})

def contact_form(request):
	if request.method=="POST":
		form=ContactForm(request.POST)
		if form.is_valid():
			message = form.save()
			global thanks
			form = ContactForm()
			thanks = 'Thanks! I will get back to you as soon as possible.'

	else:
		form = ContactForm()
		thanks = ''

	return render(request, 'thesite/contact.html', {'form':form, 'thanks':thanks,})


