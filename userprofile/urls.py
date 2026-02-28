from django.urls import path
from . import views

urlpatterns = [
    path('edit_profile_seeker',views.edit_profile_seeker,name='edit_profile_seeker'),
    path('edit_profile_recruiter',views.edit_profile_recruiter,name='edit_profile_recruiter'),
]
