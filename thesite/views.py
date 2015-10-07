from django.shortcuts import render

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