from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # adds log in/out function
    path('api-auth/', include('rest_framework.urls')), 
    path('', include('profiles.urls')),
    
]
