from django.shortcuts import render
from .models import Course, Student
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView

def home(request):
	context = {
		'courses': Course.objects.filter(instructor=request.user)
	}
	return render(request, 'gradebook/home.html', context)


def section(request, pk):
	context = {
		'students': Student.objects.filter(course_id = pk).order_by('last_name'),
	}
	return render(request, 'gradebook/student_list.html', context)

