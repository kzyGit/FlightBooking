from rest_framework import serializers
from .models.user import User
from rest_framework.validators import UniqueValidator

class UserSerializer(serializers.Serializer):
    email = serializers.EmailField(
        validators=[UniqueValidator(
            queryset=User.objects.all(),
            message='Email already registered, kindly select a different email')
        ]
    )
    first_name = serializers.CharField(min_length=3)
    middle_name = serializers.CharField(required=False, min_length=3)
    sur_name = serializers.CharField(min_length=3)
    nationality = serializers.CharField(min_length=3)
    id_or_passport = serializers.IntegerField(
        validators=[UniqueValidator(
                    queryset=User.objects.all(),
                    message='ID/passport number already registered.')
                    ]
    )
    password = serializers.CharField()

    class Meta:
        model = User
        fields = ('id', 'first_name', 'middle_name', 'sur_name', 'email',
                  'nationality', 'id_or_passport', 'password')

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    """ login serializer """
    email = serializers.EmailField()
    password = serializers.CharField()
