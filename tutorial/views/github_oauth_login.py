from django.shortcuts import redirect
from django.urls import reverse

from rest_framework.views import APIView
from tutorial.utils import github_setup


class GitHubOAuth2LoginView(APIView):
    def get(self, request):
        redirect_uri = request.build_absolute_uri(reverse("github_login_callback"))
        return redirect(github_setup(redirect_uri))
