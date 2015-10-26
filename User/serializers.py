from rest_framework import serializers
from models import *

from friendship.models import Friend
from friendship.models import Follow


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('user', 'birthday', 'gender', 'faculty', 'major', 'types', 'country', 'city')

class FriendShipSerializer(serializers.ModelSerializer):
	class Meta:
		model = Friend