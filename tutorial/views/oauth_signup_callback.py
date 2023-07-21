from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
from rest_framework.views import APIView
from tutorial.models import UserProfile
from tutorial.utils import get_user_info


class OAuth2SignupCallbackView(APIView):
    def get(self, request):
        oauth_code = request.GET["code"]

        auth_response_url = request.build_absolute_uri()
        redirect_url = request.build_absolute_uri(reverse("signup_callback"))

        # The full request URL, original redirect URL, and the returned OAuth
        # code are all necessary to send a request for user details.
        userinfo = get_user_info(auth_response_url, redirect_url, oauth_code)
        print(userinfo)

        # Extract the user profile data returned from Google.
        google_id = userinfo["sub"]
        name = userinfo["given_name"]
        email = userinfo["email"]

        # Use get_or_create since an existing user may end up signing in
        # through the sign up route.
        user, created = User.objects.get_or_create(
            username=email, defaults={"first_name": name}
        )

        # Populate the extended user data stored in UserProfile.
        UserProfile.objects.get_or_create(user=user, defaults={"google_id": google_id})

        # Here we assume that once we are logged in we should redirect to
        # the root URL and let the frontend framework routing take over.
        return HttpResponseRedirect("/")
