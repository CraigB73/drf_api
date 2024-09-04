from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')#so it can't be edited
    is_owner = serializers.SerializerMethodField() #readonly gets value with the get_is_owner
    
    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner
    class Meta:
        model= Profile
        fields = ['id', 'owner', 'updated_at', 'name', 'content', 'image', 'created_at', 'is_owner']