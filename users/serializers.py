
from rest_framework import serializers
from .models import User, ConfirmationCode
from django.contrib.auth import authenticate, get_user_model

User = get_user_model()

class ConfirmSerializer(serializers.Serializer):
    username = serializers.CharField()
    code = serializers.CharField(max_length=6)

    def validate(self, data):
        username = data.get('username')
        code = data.get('code')

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise serializers.ValidationError("Пользователь не найден.")

        if user.is_active:
            raise serializers.ValidationError("Пользователь уже активирован.")

        if user.confirmation_code != code:
            raise serializers.ValidationError("Неверный код подтверждения.")

        return data

    def save(self):
        user = User.objects.get(username=self.validated_data['username'])
        user.is_active = True
        user.confirmation_code = None
        user.save()
        return user

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data, is_active=False)
        ConfirmationCode.objects.create(user=user)
        return user


class ConfirmationSerializer(serializers.Serializer):
    username = serializers.CharField()
    code = serializers.CharField(max_length=6)

    def validate(self, data):
        try:
            user = User.objects.get(username=data['username'])
            confirm = ConfirmationCode.objects.get(user=user)
            if confirm.code != data['code']:
                raise serializers.ValidationError("Неверный код.")
            return data
        except User.DoesNotExist:
            raise serializers.ValidationError("Пользователь не найден.")
        except ConfirmationCode.DoesNotExist:
            raise serializers.ValidationError("Код подтверждения не найден.")


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(username=data['username'], password=data['password'])
        if user is None:
            raise serializers.ValidationError("Неверные данные для входа.")
        if not user.is_active:
            raise serializers.ValidationError("Пользователь не подтвержден.")
        return {"user": user}

