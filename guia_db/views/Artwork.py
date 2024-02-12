from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import AllowAny


from ..models import Artwork
from ..serializers import ArtworkSerializer

class ArtworkCreateView(APIView):
    serializer_class = ArtworkSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            serializer.data, 
            status=status.HTTP_201_CREATED
        )

class ArtworkListView(APIView):
    serializer_class = ArtworkSerializer
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        artworks = Artwork.objects.all()
        serializer = self.serializer_class(artworks, many=True)
        
        return Response(
            serializer.data, 
            status=status.HTTP_200_OK
        )