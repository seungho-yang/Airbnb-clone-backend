from rest_framework.serializers import ModelSerializer
from .models import Amenity, Room
#from users.serializers import TinyUserSerializer
from categories.serializers import CategorySerializer


class AmenitySerializer(ModelSerializer):
    class Meta:
        model = Amenity
        fields = (
            "name",
            "description",
        )


class RoomDetailSerializer(ModelSerializer):
    #owner = TinyUserSerializer(read_only=True)
    amenity = AmenitySerializer(
        read_only=True,
        many=True,
    )
    category = CategorySerializer(
        read_only = True,
    )

    class Meta:
        model = Room
        

class RoomListSerializer(ModelSerializer):
    class Meta:
        #modal = Amenity
        #fields = "__all__"
        model = Room
        fields = (
            "pk",
            "name",
            "country",
            "city",
            "price",
        )
