from rest_framework import serializers
from .models import Home, Listing_Picture, Lost_Information, Location_Information, Venue, Venue_Details
from django.contrib.auth import get_user_model


class HomeSerializers(serializers.ModelSerializer):
    class Meta:
        fields = ('author', 'images1', 'title', 'images2', 'created_at', 'update_at',)
        model = Home


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'email',)


class ListingPictureSerializers(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'images',)
        model = Listing_Picture


class LostInformationSerializers(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'category', 'title', 'datelost', 'subcategory', 'brand', 'primary_color', 'Secondary_color',
                  'description',
                  'location',)
        model = Lost_Information


class LocationInformationSerializers(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'address', 'state', 'city', 'zipcode',)
        model = Location_Information


class VenueSerializers(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'location_venue_type',)
        model = Venue


class VenueDetailsSerializers(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'venue_category', 'organization_name', 'adderss_1', 'adderss_2', 'state', 'city', 'zipcode',
                  'phone_number', 'fax_number', 'website', 'twitter',)
        model = Venue_Details
