from django.shortcuts import render, HttpResponse
from django.views.generic import View

# Create your views here.

class HomepageView(View):
    def get(self, request):
        return render(request, 'events/homepage.html')

    def post(self, request):
        pass