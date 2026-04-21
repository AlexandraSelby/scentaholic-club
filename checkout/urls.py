from django.urls import path
from .views import membership_home, create_checkout_session, success, cancel

urlpatterns = [
    path("", membership_home, name="membership"),
    path("create-checkout/", create_checkout_session, name="create_checkout"),
    path("success/", success, name="checkout_success"),
    path("cancel/", cancel, name="checkout_cancel"),
]