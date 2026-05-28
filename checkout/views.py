from django.conf import settings
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from profiles.models import Profile
import stripe


stripe.api_key = settings.STRIPE_SECRET_KEY


def membership_home(request):
    return render(request, "checkout/membership_home.html")


@login_required
def create_checkout_session(request):
    profile, created = Profile.objects.get_or_create(user=request.user)

    if profile.is_member:
        return redirect("/membership/success/")

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
        success_url=request.build_absolute_uri("/membership/success/") + "?session_id={CHECKOUT_SESSION_ID}",
        cancel_url=request.build_absolute_uri("/membership/cancel/"),
    )
    return redirect(session.url)


@login_required
def success(request):
    session_id = request.GET.get("session_id")

    if not session_id:
        return redirect("/membership/cancel/")

    try:
        session = stripe.checkout.Session.retrieve(session_id)
    except stripe.error.StripeError:
        return redirect("/membership/cancel/")

    if session.payment_status == "paid":
        profile, created = Profile.objects.get_or_create(user=request.user)
        profile.is_member = True
        profile.save()
        return render(request, "checkout/success.html")

    return redirect("/membership/cancel/")


def cancel(request):
    return render(request, "checkout/cancel.html")