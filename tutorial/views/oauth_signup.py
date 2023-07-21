from django.shortcuts import redirect
from django.urls import reverse
from rest_framework.views import APIView
from tutorial.utils import oauth2_request_uri


class OAuth2SignupView(APIView):
    def get(self, request):
        return redirect(
            oauth2_request_uri(request.build_absolute_uri(reverse("signup_callback")))
        )
