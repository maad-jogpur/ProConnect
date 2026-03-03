from django.urls import path
from . import views
urlpatterns = [
    path('register_seeker/',views.register_seeker,name='register_seeker'),
    path('register_recruiter/',views.register_recruiter,name='register_recruiter'),
    path('activate/<uidb64>/<token>',views.activate,name='activate'),
    
    path('login/',views.login,name='login'),
    path('forget_password/',views.forget_password,name='forget_password'),
    path('reset_password_validate/<uidb64>/<token>',views.reset_password_validate,name='reset_password_validate'),
    path('change_password/',views.change_password,name='change_password'),

    path('logout/',views.logout,name='logout'),
]
