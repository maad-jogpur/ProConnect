from django.urls import path
from . import views
urlpatterns = [
    path('',views.jobs,name= 'jobs'),
    path('job_detail/<int:pk>/',views.job_detail,name= 'job_detail'),
    path('apply_job/<int:pk>/',views.apply_job,name= 'apply_job'),
]
 