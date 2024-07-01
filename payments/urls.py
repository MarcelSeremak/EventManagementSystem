from django.urls import path
from . import views
from events.models import Event

urlpatterns = [
    path('cart/<int:event_id>', views.CartView.as_view(), name='cart'),
]