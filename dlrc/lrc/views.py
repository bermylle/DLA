from django.shortcuts import render
from users.decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth.decorators import login_required


def home(request):
	return render(request, 'lrc/homepage.html')


def about(request):
	return render(request, 'lrc/about.html')