from django.shortcuts import render
from rest_framework.generics import ListAPIView, ListCreateAPIView, CreateAPIView , RetrieveAPIView, UpdateAPIView, DestroyAPIView
from . import serializers as ser
from . import models as md
from rest_framework.response import Response


class BlogListView(ListAPIView):
    queryset = md.Blog.objects.all()
    serializer_class = ser.BlogSerializer


class BlogListCreateView(ListCreateAPIView):
    queryset = md.Blog.objects.all()
    serializer_class = ser.BlogSerializer


class BlogCreateView(CreateAPIView):
    queryset = md.Blog.objects.all()
    serializer_class = ser.BlogSerializer


class BlogRetriveView(RetrieveAPIView):
    queryset = md.Blog.objects.all()
    serializer_class = ser.BlogSerializer

class BlogUpdateView(UpdateAPIView):
    queryset = md.Blog.objects.all()
    serializer_class = ser.BlogSerializer


class BlogDeleteView(DestroyAPIView):
    queryset = md.Blog.objects.all()
    serializer_class = ser.BlogSerializer