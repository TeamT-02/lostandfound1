from django.urls import path
# from .views import HomeList, HomeDetail, UserList, UserDetail
from rest_framework.routers import SimpleRouter
from .views import HomeViewSet, UserViewSet, ListingPictureViewSet, LostInformationViewSet, LocationInformationViewSet, \
    VenueViewSet, VenueDetailsViewSet

router = SimpleRouter()
# Home urls page api
router.register('', HomeViewSet, basename='home')
# report url page api
router.register('users', UserViewSet, basename='users')
router.register('report/picture', ListingPictureViewSet, basename='report/picture')
router.register('report/info', LostInformationViewSet, basename='report/info')
router.register('report/location', LocationInformationViewSet, basename='report/location ')
router.register('report/venue', VenueViewSet, basename='report/venue')

# Venues url page api
router.register('venue/add/venue', VenueDetailsViewSet, basename='venue/add/venue')

urlpatterns = router.urls

# urlpatterns = [
#     path('<int:pk>/', HomeDetail.as_view()),
#     path('', HomeList.as_view()),
#     path('user/', UserList.as_view()),
#     path('user/<int:pk>/', UserDetail.as_view()),
# ]
