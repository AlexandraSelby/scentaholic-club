from django.conf import settings
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
import stripe


stripe.api_key = settings.STRIPE_SECRET_KEY


def membership_home(request):
    return render(request, "checkout/membership_home.html")


@login_required
def create_checkout_session(request):
    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=[
            {
                "price_data": {
                    "currency": "gbp",
                    "product_data": {
                        "name": "Scentaholic Weekly Sample Pack Membership",
                    },
                    "unit_amount": 500,
                    "recurring": {
                        "interval": "week",
                    },
                },
                "quantity": 1,
            }
        ],
        mode="subscription",
        success_url="http://127.0.0.1:8000/membership/success/",
        cancel_url="http://127.0.0.1:8000/membership/cancel/",
    )
    return redirect(session.url)


def success(request):
    return render(request, "checkout/success.html")


def cancel(request):
    return render(request, "checkout/cancel.html")