from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from forms import ContactForm


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
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            add = form.cleaned_data['add']
            # date = form.cleaned_data['date']
            try:
                send_mail(name, add, email, ['pselvam@conncoll.edu'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('thanks')
    return render(request, "thesite/contact.html", {'form': form})

def thanks(request):
    return HttpResponse('Thank you for your message.')