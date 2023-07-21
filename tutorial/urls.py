from django.urls import path

from .views.oauth_signup import OAuth2SignupView
from .views.oauth_signup_callback import OAuth2SignupCallbackView

urlpatterns = [
    path("signup", OAuth2SignupView.as_view(), name="signup"),
    path(
        "signup/callback/", OAuth2SignupCallbackView.as_view(), name="signup_callback"
    ),
]
