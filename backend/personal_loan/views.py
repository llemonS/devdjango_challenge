"""Views that should be exhibited through drf."""

from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from .serializers import PersonalLoanSerializer


class PersonalLoanView(ModelViewSet):
    """
    View showing personal loan details.
    """

    serializer_class = PersonalLoanSerializer
    permission_classes = (AllowAny,)
    http_method_names = ["post"]

    def post(self, request):
        """
        Post method that allows users to request a new loan.
        """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
