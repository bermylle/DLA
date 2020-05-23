from django.shortcuts import render
from users.decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth.decorators import login_required


def home(request):
	return render(request, 'lrc/homepage.html')

def about(request):
	return render(request, 'lrc/about.html')

@login_required(login_url = 'login')
@allowed_users(allowed_roles = ['admin'])
def admin(request):
	return render(request, 'lrc/dashboard.html')

def unauthorized_page(request):
	return render(request, 'lrc/401.html')