from django.shortcuts import redirect
from django.urls import reverse

from rest_framework.views import APIView
from tutorial.utils import google_setup


class GoogleOAuth2LoginView(APIView):
    def get(self, request):
        redirect_uri = request.build_absolute_uri(reverse("google_login_callback"))
        return redirect(google_setup(redirect_uri))
