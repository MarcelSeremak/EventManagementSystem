from django.shortcuts import render, HttpResponse
from django.views.generic import View, FormView
from .forms import Comment

# Create your views here.

class HomepageView(FormView):
    template_name = "events/homepage.html"
    form_class = Comment
    success_url = "/"