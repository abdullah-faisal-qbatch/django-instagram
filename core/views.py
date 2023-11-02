from rest_framework import generics
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import RegisterSerializer, MyTokenObtainPairSerializer

from .forms import SignUpForm


def frontpage(request):
    return render(request, 'core/frontpage.html')


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
