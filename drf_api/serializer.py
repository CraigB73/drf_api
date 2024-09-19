from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers

# https://dj-rest-auth.readthedocs.io/en/latest/faq.html
class CurrentUserSerializer(UserDetailsSerializer):
    profile_id = serializers.ReadOnlyField(source='profile.id')
    profile_image = serializers.ReadOnlyField(source='porfile.image.url')
    
    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + (
            'profile_id', 'profile_image'
        )