from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView

from cart.cart import Cart
from .forms import OrderCreateForm
from .models import OrderItem


# leaving these because other dependencies must be install to run weasyprint
# import weasyprint


# @staff_member_required
# def admin_order_pdf(request, order_id):
#     order = get_object_or_404(Order, id=order_id)
#     html = render_to_string('orders/order/pdf.html', {'order': order})
#
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'filename="order_{}.pdf"'.format(order.id)
#
#     weasyprint.HTML(string=html).write_pdf(response, stylesheets=[weasyprint.CSS(
#         settings.STATIC_ROOT + 'css/pdf.css')])
#     return response

class OrderCreateView(TemplateView):
    template_name = 'orders/order/create.html'
    form = OrderCreateForm

    # todo: convert it from fbv to cbv

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form = self.form(self.request.POST)

    def get_context_data(self, **kwargs):
        context = super(OrderCreateView, self).get_context_data(**kwargs)
        context['form'] = self.form()
        context['cart'] = Cart(self.request)
        return context


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
            # return render(request, 'orders/order/created.html',
            #               {'order': order})

    else:
        form = OrderCreateForm()

    return render(request, 'orders/order/create.html', {'cart': cart, 'form': form})
