from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There is nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51OYQqGJnRa2R7BliS6RiWdkUaCOvgjuUV7c3v5HoVMIsisPGOYkhmOQhNRtMMHbcoTnZXhQ2aBKONfoRGBNyI8Yg00zEGcrju1',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)