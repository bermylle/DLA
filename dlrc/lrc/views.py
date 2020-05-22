from django.shortcuts import render
from users.decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth.decorators import login_required
@login_required(login_url = 'login')
def home(request):
	return render(request, 'lrc/main.html')
	
@login_required(login_url = 'login')
def about(request):
	return render(request, 'lrc/about.html')