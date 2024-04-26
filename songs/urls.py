from django.urls import path
from .views import SongsViewset

urlpatterns = [
    path('songs', SongsViewset.as_view()),
    path('songs/<int:id>', SongsViewset.as_view())
]