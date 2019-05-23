from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
	title = models.CharField(max_length = 100)
	year = models.CharField(max_length = 100) #Spring2019, Fall2018, Winter2020
	section = models.CharField(max_length = 100) #Period 1, 00543
	instructor = models.ForeignKey(User, on_delete = models.CASCADE)

	def __str__(self):
		return self.section + " : " + self.title


class Student(models.Model):
	student_ID = models.IntegerField()
	first_name = models.CharField(max_length = 250)
	last_name = models.CharField(max_length = 250)
	email = models.EmailField()
	course = models.ForeignKey(Course, on_delete = models.CASCADE)

	def __str__(self):
		return self.first_name + " " + self.last_name

	'''
	@property
	def calculate_current_grade(self):
		return self._calculateCurrentGrade
	'''
	'''
	class Assignment(models.Model):
	student = models.ForeignKey(Student, on_delete = models.CASCADE)


	class Standard(models.Model):
		domain = CharField(max_length = 100)
		description = models.TextField()
		simple_description = models.CharField(max_length = 150)
		assignment = models.ForeignKey(Assignment, on_delete = models.PROTECT)
	'''

