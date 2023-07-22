from django.urls import path

from .views.google_oauth_signup import GoogleOAuth2SignUpView
from .views.google_oauth_signup_callback import GoogleOAuth2SignUpCallbackView
from .views.google_oauth_login import GoogleOAuth2LoginView
from .views.google_oauth_login_callback import GoogleOAuth2LoginCallbackView

from .views.github_oauth_signup import GitHubOAuth2SignUpView
from .views.github_oauth_signup_callback import GitHubOAuth2SignUpCallbackView

urlpatterns = [
    path("signup/google/", GoogleOAuth2SignUpView.as_view(), name="google_signup"),
    path(
        "signup/google/callback/",
        GoogleOAuth2SignUpCallbackView.as_view(),
        name="google_signup_callback",
    ),
    path("login/google/", GoogleOAuth2LoginView.as_view(), name="google_login"),
    path(
        "login/google/callback/",
        GoogleOAuth2LoginCallbackView.as_view(),
        name="google_login_callback",
    ),
    path("signup/github/", GitHubOAuth2SignUpView.as_view(), name="github_signup"),
    path(
        "signup/github/callback/",
        GitHubOAuth2SignUpCallbackView.as_view(),
        name="github_signup_callback",
    ),
]
