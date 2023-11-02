from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class SearchInfo(APIView):
    """
    APIView for search cars.
    """

    def get(self, request):
        """
        Get a date about car.
        Args:
        Returns:
        """
        return Response(status=status.HTTP_200_OK)
