from django.urls import path
from . import views

urlpatterns = [
    path('blog_list/', views.BlogListView.as_view(), name='blog_url'),
    path('blog_list_create/', views.BlogListCreateView.as_view(), name='blog_list_url'),
    path('blog_create/', views.BlogCreateView.as_view(), name='blog_create_url'),
    path('blog_retrive/<int:pk>/', views.BlogRetriveView.as_view(), name='blog_retrive_url'),
    path('blog_update/<int:pk>/', views.BlogUpdateView.as_view(), name='blog_update_url'),
    path('blog_delete/<int:pk>/', views.BlogDeleteView.as_view(), name='blog_delete_url'),
    path('blog_retrive_update/<int:pk>/', views.BlogRetriveUpdateView.as_view(), name='blog_retrive_update_url'),
    path('blog_retrive_destroy/<int:pk>/', views.BlogRetriveDeleteView.as_view(), name='blog_retrive_delete_url'),
    path('blog_retrive_update_delete/<int:pk>/', views.BlogRetriveUpdateDeleteView.as_view(), name='blog_retrive_update_delete_url'),

]
