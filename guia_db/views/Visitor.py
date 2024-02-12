import hashlib
import datetime

from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from rest_framework_api_key.permissions import HasAPIKey
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed, ValidationError
from django.core.exceptions import ObjectDoesNotExist

from ..authentication import token_expire_handler, expires_in, ExpiringTokenAuthentication

from ..models import Visitor
from ..serializers import VisitorSerializer

class LogVisitorApiView(APIView):
    permission_classes = [HasAPIKey]
    serializer_class = VisitorSerializer

    def post(self, request, *args, **kwargs):    
      try:
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)

        museum = serializer.validated_data['museum']
        visitor = Visitor()
        visitor.save()
        return Response(
          data = {
            'visitor_token': visitor.visitor_token
            },
          status = status.HTTP_200_OK)

      except ObjectDoesNotExist as e:
        return Response(data={
          'detail': e.args[0],
          'dev_message': 'Wrong parameter or wrong ang museum ID nga nasend.'
          }, status=status.HTTP_400_BAD_REQUEST)

      except ValidationError as e:
        return Response(
          data={
            'detail': e.detail
          }, status=status.HTTP_400_BAD_REQUEST)
