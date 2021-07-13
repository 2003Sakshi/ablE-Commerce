
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View
from django.shortcuts import render, redirect
from store.models.delivery import Delivery


class Volunteer(View):

    def get(self, request):
        #ids = list(request.session.get('cart').keys())
        deliveries = Delivery.get_all_deliveries()
        return render(request, 'volunteer.html', {'deliveries': deliveries})
