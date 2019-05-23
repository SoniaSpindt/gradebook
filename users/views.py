from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from gradebook.models import Course

@login_required
def profile(request):
	context = {
		'courses': Course.objects.filter(instructor=request.user)
	}
	return render(request, 'users/profile.html', context)
