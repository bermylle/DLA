from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required




def register(request):

	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Account created for {username}!')

			return redirect('login')
	else:
		form = CreateUserForm()

	context = {
		'form' : form
	}

	return render(request,'users/register.html', context)


@login_required
def profile(request):

	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST, instance = request.user)
		p_form = ProfileUpdateForm(request.POST, request.FILES, instance = request.user.student)

		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request, f'Account updated!')
			return redirect('profile')
	else:
		u_form = UserUpdateForm(instance = request.user)
		p_form = ProfileUpdateForm(instance = request.user.student)

	context = {
		'u_form' : u_form,
		'p_form' : p_form,
	}
	return render(request, 'users/profile.html', context)
# Kinds of messages
# messages.debug/info/success/warning/error