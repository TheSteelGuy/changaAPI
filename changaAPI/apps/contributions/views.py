from rest_framework import generics, permissions, status
from .serializers import RegistrationSerializer
from rest_framework.response import Response
from rest_framework_jwt.settings import api_settings
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model

from .renderers import UserJSONRenderer
#from .serializers import
from .models import Contribution


class RegisterUserView(generics.CreateAPIView):
    """Register a new user """
    permission_classes = (permissions.IsAuthenticated,)

    serializer_class = ContributionSerializer
    #renderer_classes = (UserJSONRenderer,)

    def post(self, request, **kwargs):
        username = request.data.get("email", "")
        password = request.data.get("password", "")
        email = request.data.get("email", "")
        user = {'username': username, 'password': password, 'email': email}

        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)

        user_obj = User.objects.create_user(
            username=username, password=password, email=email
        )

        token_serializer = TokenSerializer(data={
            # using drf jwt utility functions to generate a token
            "token": jwt_encode_handler(
                jwt_payload_handler(user_obj)
            )})
        token_serializer.is_valid(raise_exception=True)

        res = serializer.data
        res['token'] = token_serializer.data['token']

        return Response(res, status=status.HTTP_201_CREATED)


class LoginView(generics.CreateAPIView):
    """
    POST /login/
    """

    permission_classes = (permissions.AllowAny,)

    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):

        username = request.data.get("email", "")
        password = request.data.get("password", "")
        email = request.data.get("email", "")

        user = authenticate(request, email=email, password=password)
        if user is not None:
            # login saves the user’s ID in the session,
            # using Django’s session framework.
            login(request, user)
            serializer = TokenSerializer(data={
                # using drf jwt utility functions to generate a token
                "token": jwt_encode_handler(
                    jwt_payload_handler(user)
                )})
            serializer.is_valid(raise_exception=True)
            return Response(serializer.data)
        return Response({'message': 'Wrong Credentials'},status=status.HTTP_401_UNAUTHORIZED)

