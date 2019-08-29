from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MakePaymentForm, OrderForm
from .models import OrderLineItem
from django.conf import settings
from django.utils import timezone
from articles.models import Article
import stripe

# Create your views here.
stripe.api_key = settings.STRIPE_SECRET

# login_required used to ensure customer is logged in
@login_required()
def donate(request):
    
    # check to see if user is a journalist
    user = request.user
    if user.groups.filter(name='journalists').exists():
        journalist= True
    else:
        journalist= False
    
    if request.method == "POST":
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)

        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()

            
            total = int(request.POST.get('total'))
            donation_amount=str(total)
            
            try:
                customer = stripe.Charge.create(
                    # amount is multiplied by 100 as Stripe deals in cents/pennies
                    amount=int(total * 100),
                    currency="EUR",
                    description=request.user.email,
                    card=payment_form.cleaned_data['stripe_id']
                )
            except stripe.error.CardError:
                messages.error(request, "Looks like there was an issue with your card.  Unfortunately it was declined.")
                return redirect(reverse('donate'))
            
            if customer.paid:
                messages.error(request, "Thank you for your generous €"+donation_amount+" donation.  We appreciate your support.")
                request.session['cart'] = {}
                return redirect(reverse('donate'))
            else:
                messages.error(request, "Unable to take payment")
                return redirect(reverse('donate'))
        else:
            print(payment_form.errors)
            messages.error(request, "We were unable to take a payment with that card!")
    else:
        payment_form = MakePaymentForm()
        order_form = OrderForm()
    
    return render(request, "donate.html", {"order_form": order_form, "payment_form": payment_form, "publishable": settings.STRIPE_PUBLISHABLE, "journalist": journalist})