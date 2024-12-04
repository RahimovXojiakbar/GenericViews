from django.shortcuts import render
from rest_framework.generics import ListAPIView, ListCreateAPIView, CreateAPIView , RetrieveAPIView, UpdateAPIView, DestroyAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView,  RetrieveUpdateDestroyAPIView
from . import serializers as ser
from . import models as md
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination



class Paginatsiya_fields(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 100

class BlogListView(ListAPIView):
    queryset = md.Blog.objects.all()
    serializer_class = ser.BlogSerializer
    pagination_class = Paginatsiya_fields



class BlogListCreateView(ListCreateAPIView):
    queryset = md.Blog.objects.all()
    serializer_class = ser.BlogSerializer
    pagination_class = Paginatsiya_fields



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

class BlogRetriveUpdateView(RetrieveUpdateAPIView):
    queryset = md.Blog.objects.all()
    serializer_class = ser.BlogSerializer


class BlogRetriveDeleteView(RetrieveDestroyAPIView):
    queryset = md.Blog.objects.all()
    serializer_class = ser.BlogSerializer


class BlogRetriveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = md.Blog.objects.all()
    serializer_class = ser.BlogSerializer





