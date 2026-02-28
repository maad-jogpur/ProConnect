from django.urls import path
from . import views
urlpatterns = [
    path('',views.jobs,name= 'jobs'),
    path('search_jobs/',views.search_jobs,name= 'search_jobs'),
    path('job_detail/<int:pk>/',views.job_detail,name= 'job_detail'),
    path('apply_job/<int:pk>/',views.apply_job,name= 'apply_job'),
]
 