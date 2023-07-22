from django.contrib.auth.models import User

from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls import reverse

from requests_oauthlib import OAuth2Session
from rest_framework.views import APIView
from tutorial.models import UserProfile


class GitHubOAuth2SignUpCallbackView(APIView):
    def get(self, request):
        redirect_uri = request.build_absolute_uri(reverse("github_signup_callback"))

        session = OAuth2Session(settings.GITHUB_CLIENT_ID)
        authorization_response = request.build_absolute_uri()

        session.fetch_token(
            settings.GITHUB_TOKEN_URL,
            client_secret=settings.GITHUB_CLIENT_SECRET,
            authorization_response=authorization_response,
        )

        user_data = session.get("https://api.github.com/user").json()

        # Use get_or_create since an existing user may end up signing in
        # through the sign up route.
        user, created = User.objects.get_or_create(username=user_data["login"])

        # Populate the extended user data stored in UserProfile.
        UserProfile.objects.get_or_create(
            user=user, defaults={"github_id": user_data["id"]}
        )

        # Here we assume that once we are logged in we should redirect to
        # the root URL and let the frontend framework routing take over.
        return HttpResponseRedirect("/")
