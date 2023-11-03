from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from swagger.schema import get_date_cars_schema
from swagger.serialiser import SearchCarSerialiserSwagger


class SearchInfo(APIView):
    """
    APIView for search cars.
    """

    @swagger_auto_schema(
        request_method="POST",
        request_body=SearchCarSerialiserSwagger,
        responses={
            "200": openapi.Response(description="OK", schema=get_date_cars_schema),
            "404": openapi.Response(description="Date not found"),
            "500": openapi.Response(description="Internal Server Error"),
        },
        operation_summary="Get a date about cars",
    )
    def post(self, request):
        """
        Get a date about car.
        Args:
        Returns:
        """
        return Response(status=status.HTTP_200_OK)
