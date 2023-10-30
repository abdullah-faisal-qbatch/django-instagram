from django.http import HttpResponse
from rest_framework.viewsets import ReadOnlyModelViewSet
# Create your views here.
from rest_framework.viewsets import ReadOnlyModelViewSet


class PostingView(ReadOnlyModelViewSet):
    def get(self, request):
        return HttpResponse("GET PostingView: Hello World")

    def post(self, request):
        return HttpResponse("POST PostingView: Hello World")
