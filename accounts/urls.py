from django.urls import path
from . import views
urlpatterns = [
    path('register_seeker/',views.register_seeker,name='register_seeker'),
    path('register_recruiter/',views.register_recruiter,name='register_recruiter'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
]
