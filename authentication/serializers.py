from datetime import date

from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for User model.
    """

    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    def validate_date_of_birth(self, value):
        """Validate user is at least 15 years old (GDPR requirement)."""
        today = date.today()
        age = (
            today.year
            - value.year
            - ((today.month, today.day) < (value.month, value.day))
        )

        if age < 15:
            raise serializers.ValidationError("User must be at least 15 years old.")

        return value

    def validate(self, data):
        """Check if passwords match."""
        password = data.get("password")
        password2 = data.get("password2")
        if password or password2:
            if password != password2:
                raise serializers.ValidationError(
                    {"password": "Passwords don't match."}
                )
        return data

    def create(self, validated_data):
        """Create a new user with encrypted password."""
        validated_data.pop("password2")
        return User.objects.create_user(**validated_data)

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "password",
            "password2",
            "date_of_birth",
            "can_be_contacted",
            "can_data_be_shared",
            "age",
        ]
        read_only_fields = ["id", "age"]
