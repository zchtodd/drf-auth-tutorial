import json

import requests
from django.conf import settings
from oauthlib.oauth2 import WebApplicationClient


def get_google_provider_cfg():
    return requests.get(
        "https://token.actions.githubusercontent.com/.well-known/openid-configuration"
    ).json()
    # return requests.get(
    #     "https://accounts.google.com/.well-known/openid-configuration"
    # ).json()


def oauth2_request_uri(redirect_uri):
    google_provider_cfg = get_google_provider_cfg()
    authorization_endpoint = google_provider_cfg["authorization_endpoint"]

    client = WebApplicationClient(settings.GITHUB_CLIENT_ID)

    return client.prepare_request_uri(
        authorization_endpoint,
        redirect_uri=redirect_uri,
        scope=["openid", "email", "profile"],
    )


def get_user_info(auth_response_url, redirect_url, oauth_code):
    google_provider_cfg = get_google_provider_cfg()
    token_endpoint = google_provider_cfg["token_endpoint"]

    client = WebApplicationClient(settings.GITHUB_CLIENT_ID)

    token_url, headers, body = client.prepare_token_request(
        token_endpoint,
        authorization_response=auth_response_url,
        redirect_url=redirect_url,
        code=oauth_code,
    )

    token_response = requests.post(
        token_url,
        headers=headers,
        data=body,
        auth=(settings.GITHUB_CLIENT_ID, settings.GITHUB_CLIENT_SECRET),
    )

    client.parse_request_body_response(json.dumps(token_response.json()))

    userinfo_endpoint = google_provider_cfg["userinfo_endpoint"]
    uri, headers, body = client.add_token(userinfo_endpoint)
    userinfo_response = requests.get(uri, headers=headers, data=body)

    return userinfo_response.json()
