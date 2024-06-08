from rest_framework import viewsets
from django.shortcuts import get_object_or_404, redirect
from . import models
from . import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet


class SongsViewset(APIView):
    def get(self, request, id=None):
        if id:
            item = models.Songs.objects.get(id=id)
            serializer = serializers.SongsSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        items = models.Songs.objects.all()
        serializer = serializers.SongsSerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = serializers.SongsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id=None):
        item = models.Songs.objects.get(id=id)
        serializer = serializers.SongsSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None):
        item = models.Songs.objects.filter(id=id)
        print(item)
        item.delete()
        return Response({"status": "success", "data": "Item Deleted"})
    
class SpotifyRequestUserAuthorization(GenericViewSet):
    permission_classes = (AllowAny,)

    def list(self, request):
        #ID from Spotify dashboard
        client_id = "03972d2d7adf4ae59d91c882b4350d17"

        # Required argument. It must be the string code.
        response_type = "code"

        # Required argument. This is the Redirect URI configured on the dashbaord.
        redirect_uri = "http://localhost:8080/api/spotify/callback"

        # The scopes to request from the user. This is a space-separated list.
        scope = "user-modify-playback-state"

        # Optional. User identificiation
        state = "colinfong"

        # The Spotify API base URL
        base_url = "https://accounts.spotify.com/authorize"

        # The url to redirect the user id
        url = (
            f"{base_url}?response_type={response_type}&client_id={client_id}&redirect_uri={redirect_uri}&scope={scope}"
            f"&state={state}"
        )
        
        return redirect(url)

def store_code(code:str, user_id: str):
    serializer = serializers.TokenSerializer(access_token = code, user = user_id)
    if serializer.is_valid():
        serializer.save()
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    else:
        return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
class SpotifyCallback(GenericViewSet):
    permission_classes = (AllowAny,)

    def list(self, request):
        code = request.query_params.get("code")

        state = request.query_params.get("state")

        store_code(code, state)
        return Response(status=status.HTTP_200_OK, data={"code": code})