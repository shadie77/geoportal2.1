from django.contrib.auth.models import User
from django.db.models import fields
from rest_framework import serializers
from .models import UserProfileInfo
from rest_framework.authtoken.models import Token
from .models import Route, Jetty, Bathy, Depth, Water_Boundary, Ridership, Accident, Jetty_Pictures
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from django.contrib.auth.models import User


class UserInfoSerializer(serializers.ModelSerializer): 
    class Meta:
        model = UserProfileInfo
        fields= ['department', 'phone_number', 'profile_pic', 'created_at']

class UserSerializer(serializers.ModelSerializer):
    profile = UserInfoSerializer(many=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'profile']
        depth= 2

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user

class jettySerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Jetty
        geo_field = "geom"
        fields = "__all__"


class bathySerializer(GeoFeatureModelSerializer):
    class Meta:
        model= Bathy
        geo_field = "geom"
        fields= "__all__"

class routeSerializer(GeoFeatureModelSerializer):
	class Meta:
		model = Route
		geo_field = "geom"
		fields = "__all__"

class depthSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Depth
        geo_field = "geom"
        fields = "__all__"

class boundarySerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Water_Boundary
        geo_field = "geom"
        fields = "__all__"

class ridershipSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Ridership
        fields= "__all__"

class accidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accident
        fields = "__all__"

class jettyPictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jetty_Pictures
        fields = ['jetty_id', 'medium_picture']

