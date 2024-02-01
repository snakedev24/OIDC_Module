from oauth2_provider.views.generic import ProtectedResourceView
from django.http import HttpResponse

class ApiEndpoint(ProtectedResourceView):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, OAuth2!')

from django.contrib.auth.decorators import login_required
# from django.http.response import HttpResponse

@login_required()
def secret_page(request, *args, **kwargs):
    return HttpResponse('Secret contents!', status=200)

from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# @csrf_excempt
class YourListView(APIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    def get(self, request, *args, **kwargs):

            # Customize the data you want to include in the response
        data = {
            'id': 7,
            'name': "48",
            # Add other fields as needed
        }

        return Response(data, status=status.HTTP_200_OK)