from rest_framework import serializers
from .models import Profile
from followers.models import Follower

class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')#so it can't be edited
    is_owner = serializers.SerializerMethodField() #readonly gets value with the get_is_owner
    following_id = serializers.SerializerMethodField()
    post_count = serializers.ReadOnlyField()
    followers_count = serializers.ReadOnlyField()
    following_count = serializers.ReadOnlyField()
    
    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner
    
    def get_following_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            following = Follower.objects.filter(
                owner=user, followed=obj.owner
            ).first()
            return following.id if following else None
        return None
            
    class Meta: 
        model= Profile
        fields = ['id', 'owner', 'updated_at', 'name', 
                  'content', 'image', 'created_at', 'is_owner', 'following_id',
                  'post_count', 'followers_count', 'following_count'
                  ]