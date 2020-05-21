from django.shortcuts import render


def home(request):
	return render(request, 'lrc/main.html')

def about(request):
	return render(request, 'lrc/about.html')