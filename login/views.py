from django.shortcuts import render, HttpResponse
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from rest_auth.registration.views import SocialLoginView
from django.contrib.auth.decorators import login_required


# Create your views here.
class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter


def login(request):
    return render(request, 'login/login.html')

@login_required
def home(request):
    return HttpResponse("Hello, logged in user!")