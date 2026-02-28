from django.urls import path

from . import views


urlpatterns = [
    path('recruiter/',views.recruiter_dashboard,name = 'recruiter_dashboard'),
    path('recruiter/post_job',views.post_job,name = 'post_job'),
    path('recruiter/edit_job/<int:pk>/',views.edit_job,name = 'edit_job'),
    path('recruiter/delete_job/<int:pk>/',views.delete_job,name = 'delete_job'),
    path('recruiter/view_applicants/<int:pk>/',views.view_applicants,name = 'view_applicants'),
    path('select_applicant/<int:pk>/',views.select_applicant,name = 'select_applicant'),
    path('reject_applicant/<int:pk>/',views.reject_applicant,name = 'reject_applicant'),

    path('seeker/',views.seeker_dashboard,name = 'seeker_dashboard'),
]
