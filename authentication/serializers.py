from datetime import date

from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for User model.
    """

    def validate_date_of_birth(self, value):
        today = date.today()
        age = today.year - value.year - (
            (today.month, today.day) < (value.month, value.day)
        )

        if age < 15:
            raise serializers.ValidationError(
                "User must be at least 15 years old."
            )

        return value

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
            'date_of_birth',
            'can_be_contacted',
            'can_data_be_shared',
            'age'
        ]
        read_only_fields = ['id', 'age']
