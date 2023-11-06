from rest_framework import generics
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import RegisterSerializer, MyTokenObtainPairSerializer

from .forms import SignUpForm
import requests


def frontpage(request):
    return render(request, 'core/frontpage.html')


def login_method(request):

    if (request.method == 'GET'):
        print("Performed GET request!")
        # Perform the process of access token and refresh token here

        # request.COOKIES.get("refresh_token")
        print('Access Token', request.COOKIES.get("access_token"))
        print('Refresh Token', request.COOKIES.get("refresh_token"))
        return render(request, 'core/login.html')

    if request.method == 'POST':
        # print("Performed POST request!")
        url = "http://127.0.0.1:8000/auth/login/"

        username = request.POST.get('username')
        password = request.POST.get('password')

        data = {
            "username": username,
            "password": password
        }

        # Send a POST request with JSON data
        response = requests.post(url, json=data)
        # Check the response
        if response.status_code == 200:
            # Request was successful, and you can work with the response data
            print("POST request was successful")
            response_sender = render(request, 'core/frontpage.html',
                                     {'context_data': 'value'})
            response_sender.set_cookie(
                'access_token', response.json()['access'])
            response_sender.set_cookie(
                'refresh_token', response.json()['refresh'])
            return response_sender
        else:
            # Request failed
            print(
                f"POST request failed with status code {response.status_code}")
            print("Response content:", response.text)
            import json
            return HttpResponse(json.loads(response.text)['detail'])

    #     form = SignUpForm(request.POST)

    #     if form.is_valid():
    #         user = form.save()

    #         login(request, user)

    #         return redirect('frontpage')
    # else:
    #     form = SignUpForm()

    # return render(request, 'core/signup.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('frontpage')
    else:
        form = SignUpForm()

    return render(request, 'core/signup.html', {'form': form})


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
    template_name = 'core/signup.html'

    def get(self, request, *args, **kwargs):
        return render(request, 'core/signup.html',)

    def post(self, request, *args, **kwargs):
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            # Log the user in
            login(request, user)

            return redirect('frontpage')

        return render(request, self.template_name, {'form': form})
