from django.urls import path
from profiles import views

urlpatterns = [
    path('profiles/', views.ProfileList.as_view()),
    path('profiles/<int:pk>/', views.ProfileDetailView.as_view())
]


#<int:pk> = uses a primary key in the form of a interger from the profiles