from django.urls import path
from .views import SongsViewset
from .views import SpotifyRequestUserAuthorization

urlpatterns = [
    path('songs', SongsViewset.as_view()),
    path('songs/<int:id>', SongsViewset.as_view()),
    path('login', SpotifyRequestUserAuthorization.as_view({'get': 'list'}))
]