from rest_framework import serializers
from django.core.validators import RegexValidator
from .models import User


class RegistrationSerializer(serializers.ModelSerializer):
    """User Serialization class."""

    # Ensure passwords are at least 8 characters long, no longer than 128
    # characters, and can not be read by the client.
    reval = RegexValidator(r"\d+", "Password must contain at least one digit")
    password = serializers.CharField(
        max_length=128,
        min_length=4,
        write_only=True,
        validators=[reval]
    )

    # The client should not be able to send a token along with a registration
    # request. Making `token` read-only handles that for us.
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        # List all of the fields that could possibly be included in a request
        # or response, including fields specified explicitly above.
        fields = ['email', 'username', 'password', 'token']


class TokenSerializer(serializers.Serializer):
    """
    This serializer serializes the token data
    """
    token = serializers.CharField(max_length=255)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email")


