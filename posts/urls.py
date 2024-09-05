from django.urls import path
from posts import views

urlpatterns = [
    path('post/', views.PostList.as_view())
]