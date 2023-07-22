from django.contrib.auth.models import User

from django.http import JsonResponse
from django.urls import reverse

from rest_framework.authtoken.models import Token
from rest_framework.views import APIView

from tutorial.utils import google_callback


class GoogleOAuth2LoginCallbackView(APIView):
    def get(self, request):
        redirect_uri = request.build_absolute_uri(reverse("google_login_callback"))
        auth_uri = request.build_absolute_uri()

        user_data = google_callback(redirect_uri, auth_uri)

        try:
            user = User.objects.get(username=user_data["email"])
        except User.DoesNotExist:
            return JsonResponse({"error": "User does not exist. Please sign up first."}, status=400)

        # Create the auth token for the frontend to use.
        token, _ = Token.objects.get_or_create(user=user)

        # Here we assume that once we are logged in we should send
        # a token to the frontend that a framework like React or Angular
        # can use to authenticate further requests.
        return JsonResponse({"token": token.key})
