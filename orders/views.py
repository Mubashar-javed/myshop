from django.http.request import HttpRequest
from cart.cart import Cart
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import TemplateView

from .forms import OrderCreateForm
from .models import OrderItem


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            if cart.coupon:
                order.coupon = cart.coupon
                order.discount = cart.coupon.discount
            order.save()
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'],
                                         price=item['price'], quantity=item['quantity'])
            # clear the cart
            cart.clear()
            subject = "order number  is {}".format(order.id)
            message = f"Dear {order.first_name}  your order has been places successfly!"
            send_mail(subject, message, 'myshop@admin.com', [order.email])

            request.session['order_id'] = order.id
            # redirect for payments
            return redirect(reverse('payment: process'))

    else:
        form = OrderCreateForm()

    return render(request, 'orders/order/create.html', {'cart': cart, 'form': form})
