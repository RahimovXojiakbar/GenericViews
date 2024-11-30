from django.urls import path
from . import views

urlpatterns = [
    path('bloglist/', views.BlogListView.as_view(), name='blog_url'),
    path('bloglistcreate/', views.BlogListCreateView.as_view(), name='blog_list_url'),
    path('blogcreate/', views.BlogCreateView.as_view(), name='blog_create_url'),
    path('blogretrive/<int:pk>/', views.BlogRetriveView.as_view(), name='blog_retrive_url'),
    path('blogupdate/<int:pk>/', views.BlogUpdateView.as_view(), name='blog_update_url'),
    path('blogdelete/<int:pk>/', views.BlogDeleteView.as_view(), name='blog_delete_url')

]
