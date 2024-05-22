from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.views.generic import View, FormView
from django.urls import reverse_lazy
from .forms import Comment

# Create your views here.

class HomepageView(FormView):
    template_name = "events/homepage.html"
    form_class = Comment
    success_url = "/"

class RegisterView(FormView):
    template_name = 'events/registration.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('homepage')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)

class LoginView(FormView):
    template_name = 'events/login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('homepage')

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return super().form_valid(form)

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')