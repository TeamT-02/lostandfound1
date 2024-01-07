from django.urls import path
# from .views import HomeList, HomeDetail, UserList, UserDetail
from rest_framework.routers import SimpleRouter
from .views import HomeViewSet, UserViewSet, ListingPictureViewSet

router = SimpleRouter()
router.register('users', UserViewSet, basename='users')
router.register('', HomeViewSet, basename='home')
router.register('list/picture', ListingPictureViewSet, basename='list/picture')

urlpatterns = router.urls









# urlpatterns = [
#     path('<int:pk>/', HomeDetail.as_view()),
#     path('', HomeList.as_view()),
#     path('user/', UserList.as_view()),
#     path('user/<int:pk>/', UserDetail.as_view()),
# ]
