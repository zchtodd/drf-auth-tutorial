from django.conf import settings
from django.shortcuts import redirect
from django.urls import reverse

from requests_oauthlib import OAuth2Session
from rest_framework.views import APIView


class GitHubOAuth2SignUpView(APIView):
    def get(self, request):
        redirect_uri = request.build_absolute_uri(reverse("github_signup_callback"))
        session = OAuth2Session(settings.GITHUB_CLIENT_ID)

        authorization_url, state = session.authorization_url(settings.GITHUB_AUTH_URL)
        return redirect(authorization_url)
