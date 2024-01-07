from .serializers import HomeSerializers, UserSerializers, ListingPictureSerializers
from rest_framework.viewsets import ModelViewSet
from .models import Home, Listing_Picture
from .permissions import IsAuthorOrReadOnly
from django.contrib.auth import get_user_model


#
# class HomeList(ListCreateAPIView):
#     queryset = Home.objects.all()
#     serializer_class = HomeSerializers
#
#
# class HomeDetail(RetrieveUpdateDestroyAPIView):
#     permission_classes = (IsAuthorOrReadOnly,)
#     queryset = Home.objects.all()
#     serializer_class = HomeSerializers
#
#
# class UserList(ListCreateAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializers
#
#
# class UserDetail(RetrieveUpdateDestroyAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializers


# kerakli tekadagilar prosta codeni qisqarterdm bu code uzin bub ketgani uchun va uzimga qulayroq qildm


class HomeViewSet(ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Home.objects.all()
    serializer_class = HomeSerializers


class UserViewSet(ModelViewSet):
    # permission_classes = (IsAuthorOrReadOnly)
    queryset = get_user_model().objects.all
    serializer_class = UserSerializers


class ListingPictureViewSet(ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Listing_Picture.objects.all()
    serializer_class = ListingPictureSerializers
