from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.views.generic import View, FormView, CreateView, ListView, DetailView
# Create your views here.

class ContactView(View):
    def get(self, request):
        return render(request, 'reports/contact.html')

    def post(self, request):

        # Change this so it sends emails

        # name = request.POST.get('name')
        # email = request.POST.get('email')
        # subject = request.POST.get('subject')
        # message = request.POST.get('message')
        #
        # send_mail(
        #     subject,
        #     message,
        #     settings.DEFAULT_FROM_EMAIL,
        #     [settings.CONTACT_EMAIL],
        #     fail_silently=False,
        # )
        #

        messages.success(request, 'Your message has been sent successfully!')
        return redirect('contact')
