from django.contrib.auth.models import User

from django.http import JsonResponse
from django.urls import reverse

from rest_framework.authtoken.models import Token
from rest_framework.views import APIView

from tutorial.utils import google_callback
from tutorial.models import UserProfile


class GoogleOAuth2SignUpCallbackView(APIView):
    def get(self, request):
        redirect_uri = request.build_absolute_uri(reverse("google_signup_callback"))
        auth_uri = request.build_absolute_uri()

        user_data = google_callback(redirect_uri, auth_uri)

        # Use get_or_create since an existing user may end up signing in
        # through the sign up route.
        user, _ = User.objects.get_or_create(
            username=user_data["email"],
            defaults={"first_name": user_data["given_name"]},
        )

        # Populate the extended user data stored in UserProfile.
        UserProfile.objects.get_or_create(
            user=user, defaults={"google_id": user_data["id"]}
        )

        # Create the auth token for the frontend to use.
        token, _ = Token.objects.get_or_create(user=user)

        # Here we assume that once we are logged in we should send
        # a token to the frontend that a framework like React or Angular
        # can use to authenticate further requests.
        return JsonResponse({"token": token.key})
