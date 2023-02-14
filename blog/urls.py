from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name = 'post_list'),
    path('post/<int:pk>/', views.post_detail, name = 'post_detail'),
    path('post/new/', views.post_new, name = 'post_new'),
    path('post/<int:pk>/edit', views.post_edit, name = 'post_edit'),
    ]

# matches empty string (ignoring domain name, https:\\sushanthrao.pythonanywhere.com\) and redirects it to view path_list
# basically, the above pattern will tell Django to resolve Root URL to path_list
