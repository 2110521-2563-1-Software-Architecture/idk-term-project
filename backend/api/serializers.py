from rest_framework import serializers

from linkurl.models import Link
from users.models import CustomUser

class LinkSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Link
        # fields = '__all__'
        fields = ['link_shorten','link_original','link_user']

    def create(self, validated_data):
        links = Link.objects.create(link_shorten=validated_data.pop('link_shorten'),
                                    link_original=validated_data.pop('link_original'),
                                    link_user=validated_data.pop('link_user'))
        links.save()
        return links

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

    def create(self, validated_data):
        user = CustomUser.objects.create_user(user_name=validated_data.pop('user_name'), 
                                              password=validated_data.pop('password'),
                                              user_email=validated_data.pop('user_email'))
        user.save()
        return user