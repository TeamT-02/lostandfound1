from rest_framework import serializers
from .models import Home, Listing_Picture
from django.contrib.auth import get_user_model


class HomeSerializers(serializers.ModelSerializer):
    class Meta:
        fields = ('author', 'images1', 'title', 'images2', 'created_at', 'update_at',)
        model = Home


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username')


class ListingPictureSerializers(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'images',)
        model = Listing_Picture
