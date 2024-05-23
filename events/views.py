from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.views.generic import View, FormView
from django.urls import reverse_lazy
from .forms import CommentForm, CustomUserCreationForm
from .models import Comment

# Create your views here.

class HomepageView(FormView):
    template_name = "events/homepage.html"
    form_class = CommentForm
    success_url = "/"
    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.user = self.request.user
        comment.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comment_first"] = Comment.objects.order_by("-id")[0]
        context["comments"] = Comment.objects.order_by("-id")[1:4]
        return context

class RegisterView(FormView):
    template_name = 'events/registration.html'
    form_class = CustomUserCreationForm
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
        return redirect('homepage')