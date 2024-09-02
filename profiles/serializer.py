from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')#so it can't be edited
    
    class Meta:
        model= Profile
        fields = ['id', 'owner', 'created_at', 'updated_at', 'name', 'content', 'image']