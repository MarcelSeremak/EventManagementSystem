from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, FormView, CreateView, ListView, DetailView
from .models import Ticket
from events.models import Event
# Create your views here.

class CartView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        event = get_object_or_404(Event, pk=self.kwargs['event_id'])

        # Create and save the new ticket
        ticket_from_now = Ticket(event=event, user=request.user)
        ticket_from_now.save()

        # Fetch all tickets for the current user
        user_tickets = Ticket.objects.filter(user=request.user)

        total_amount=0
        for ticket in user_tickets:
            total_amount += float(ticket.event.price)
        context = {
            'user_tickets': user_tickets,
            'total_amount': total_amount
        }
        return render(request, 'payments/cart.html', context)