from typing import Any
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.models import Group
from django.views import View
from .forms import RegisterForm
from django.views.generic import TemplateView
# Create your views here.
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.views import PasswordResetView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from .models import Course

from django.utils.decorators import method_decorator



class CustomeTemplateView(TemplateView):
    group_name = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        if user.is_authenticated:
            group = Group.objects.filter(user = user).first()
            if group:
                self.group_name = group.name


        context['group_name']= self.group_name
        return context











class HomeView(CustomeTemplateView):

    template_name = 'home.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        group_name = None
        if user.is_authenticated:
            group = Group.objects.filter(user=user).first()
            if group:
                group_name = group.name

        context['group_name'] = group_name
        return context
      


class PrecingView(CustomeTemplateView):
    template_name = 'precing.html'



class RegisterView(View):
   def get(self, request):
       data = {
           

           'form': RegisterForm()
       }
       return render(request,'registration/register.html', data)
   
   def post(self,request):
       user_creation_form = RegisterForm(data= request.POST)
       if user_creation_form.is_valid():
           user_creation_form.save()
           user = authenticate(username = user_creation_form.cleaned_data['username'], password = user_creation_form.cleaned_data['password1'])
           login(request, user)
           return redirect('home')
       
       data = {
           

           'form': user_creation_form
       }
       return render(request, 'registration/register.html',data)
   



class ProfilePasswordChangeView(PasswordChangeView):
    template_name = 'registration/change_password.html'
    success_url = reverse_lazy('login')
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['password_change'] = self.request.session.get('password_change', False)
        return context
    
    def form_valid(self, form):
        messages.success(self.request,'Cambio de contraseña exitoso')
        update_session_auth_hash(self.request,form.user)
        self.request.session['password_change']= True
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request,'No se puede cambiar las contraseña')
        
        return super().form_invalid(form)
    



class ProfileView(CustomeTemplateView):
    template_name = 'profile/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user  = self.request.user
        return context
    




# mostara los cursos
    
class CoursesView(TemplateView):

    template_name = 'courses.html'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        courses = Course.objects.all()
        context['courses'] = courses

        return context
    


    

