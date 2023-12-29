from django.urls import path
from .views import HomeView, PrecingView, RegisterView , ProfileView ,CoursesView
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns =[


    path('',HomeView.as_view(), name = 'home'),
    path('precing/',PrecingView.as_view(), name = 'precing'),
    path('register/',RegisterView.as_view(), name = 'register'),


    path('profile/',ProfileView.as_view(), name = 'profile'),
    path('courses/',CoursesView.as_view(), name = 'courses'),

    path('password_change/', login_required(ProfilePasswordChangeView.as_view()) , name='profile_password_change'),
    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),

    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),

    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),

    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),

]   