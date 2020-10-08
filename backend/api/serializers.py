from rest_framework import serializers

from linkurl.models import Link
from users.models import CustomUser

class LinkSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Link
        fields = '__all__'

    def create(self, validated_data):
        link_shorten = validated_data.pop('link_shorten')
        link_original = validated_data.pop('link_original')
        link_user = validated_data.pop('link_user')
        
        links = Link.objects.create(link_shorten=link_shorten,
                                    link_original=link_original,
                                    link_user=link_user)
        links.save()
        return links