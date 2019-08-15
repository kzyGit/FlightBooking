from rest_framework.generics import (
    ListAPIView, ListCreateAPIView, CreateAPIView)
from rest_framework.response import Response
from rest_framework import status
from api.serializers import UserSerializer, LoginSerializer
from ..models import User
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate, login

from rest_framework_jwt.settings import api_settings
from ..helpers.validators import validate_password

from ..helpers.cloudinary import upload_images

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class HomeView(ListAPIView):
    """ Home route """

    def get(self, request):
        return Response("Welcome to Flight Booking API")


class UserView(ListCreateAPIView):
    """ User account endpoint """
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            validate_password(request.data['password'])
            try:
                upload = upload_images(request.data['image'])
                serializer.save(image=upload['url'])
            except Exception:
                serializer.save()
            data = {
                'message': 'User Signed Up successfully',
                'data': serializer.data
            }
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(CreateAPIView):
    """ login Viewset """
    serializer_class = LoginSerializer

    def post(self, request):
        user = request.data
        serializer = LoginSerializer(data=user)
        serializer.is_valid(raise_exception=True)
        result = authenticate(request, username=user['email'],
                              password=user['password'])
        if result:
            login(request, result)
            token = jwt_encode_handler(jwt_payload_handler(result))
            data = {
                'message': 'User logged in successfully',
                'token': token
            }
            code = status.HTTP_200_OK
        else:
            data = {
                'message': 'Invalid Login credentials'
            }
            code = status.HTTP_401_UNAUTHORIZED
        return Response(data, status=code)
