import secrets
import string
from rest_framework import serializers
from .models import BetterLink, ProtocolChoices


class BetterLinkSerializer(serializers.ModelSerializer):
    long_link = serializers.CharField(write_only=True)
    short_link = serializers.CharField(required=False)

    class Meta:
        model = BetterLink
        fields = ('long_link', 'short_link')

    def validate_short_link(self, value):
        if BetterLink.objects.filter(short_link=value).exists():
            raise serializers.ValidationError("Short link already exists in the database.")
        return value

    def create(self, validated_data):
        long_link = validated_data.get('long_link')
        short_link = validated_data.get('short_link')
        if not short_link:
            short_link_length = 4
            short_link = ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(short_link_length))
            while BetterLink.objects.filter(short_link=short_link).exists():
                short_link = ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(short_link_length))
        instance = BetterLink.objects.create(
            old_long_link_proto=ProtocolChoices.HTTP if long_link.startswith('http://') else ProtocolChoices.HTTPS,
            old_link_url=long_link.split("://")[1],
            short_link=short_link
        )
        return instance

    def to_representation(self, instance):
        return instance.view
