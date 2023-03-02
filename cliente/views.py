from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.views import APIView
from .serializers import UserCreateSerializer, UserSerializer


class RegisterView(APIView):
    def post(self, request):
        data = request.data

        if 'email' in data:
            serializer = UserCreateSerializer(data=data)
        elif 'username' in data:
            serializer = UserCreateSerializer(data=data, context={'username': True})
        else:
            return Response({'error': 'Either email or username is required'}, status=status.HTTP_400_BAD_REQUEST)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        user = serializer.save()

        user_serializer = UserSerializer(user)
        return Response(user_serializer.data, status=status.HTTP_201_CREATED)


class RetrieveUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user

        user_serializer = UserSerializer(user)
        return Response(user_serializer.data, status=status.HTTP_200_OK)
