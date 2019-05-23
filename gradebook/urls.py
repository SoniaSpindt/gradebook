from django.urls import path
#from .views import StudentListView
from django.contrib.auth import views as auth_views
from users import views as user_views
from . import views

urlpatterns = [
    path('', views.home, name='gradebook-home'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login' ),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout' ),
    path('profile/', user_views.profile, name='profile' ),
    path('section/<int:pk>/', views.section, name='student-list'),
]

#path('section/<int:pk>/', StudentListView.as_view(), name='student-list'),