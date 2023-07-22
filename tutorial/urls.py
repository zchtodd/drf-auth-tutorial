from django.urls import path

from .views.google_oauth_signup import GoogleOAuth2SignUpView
from .views.google_oauth_signup_callback import GoogleOAuth2SignUpCallbackView
from .views.google_oauth_login import GoogleOAuth2LoginView
from .views.google_oauth_login_callback import GoogleOAuth2LoginCallbackView

from .views.github_oauth_signup import GitHubOAuth2SignUpView
from .views.github_oauth_signup_callback import GitHubOAuth2SignUpCallbackView
from .views.github_oauth_login import GitHubOAuth2LoginView
from .views.github_oauth_login_callback import GitHubOAuth2LoginCallbackView

urlpatterns = [
    path("signup/google/", GoogleOAuth2SignUpView.as_view(), name="google_signup"),
    path(
        "google/callback/signup",
        GoogleOAuth2SignUpCallbackView.as_view(),
        name="google_signup_callback",
    ),
    path("login/google/", GoogleOAuth2LoginView.as_view(), name="google_login"),
    path(
        "google/callback/login",
        GoogleOAuth2LoginCallbackView.as_view(),
        name="google_login_callback",
    ),
    path("signup/github/", GitHubOAuth2SignUpView.as_view(), name="github_signup"),
    path(
        "github/callback/signup",
        GitHubOAuth2SignUpCallbackView.as_view(),
        name="github_signup_callback",
    ),
    path("login/github/", GitHubOAuth2LoginView.as_view(), name="github_login"),
    path(
        "github/callback/login/",
        GitHubOAuth2LoginCallbackView.as_view(),
        name="github_login_callback",
    ),
]
