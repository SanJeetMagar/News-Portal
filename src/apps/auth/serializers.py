from rest_framework import serializers
from django.db import transaction
from .models import User, Role



class UserRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email", "password", "role", "phone")

    def create(self, validated_data):
        first_name = validated_data.get("first_name", None)
        last_name = validated_data.get("last_name", None)
        username = validated_data.get("username", None)
        email = validated_data.get("email", None)
        password = validated_data.get("password", None)
        role = validated_data.get("role", Role.ADMIN)
        phone = validated_data.get("phone", None)
        with transaction.atomic():
            user: User = User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                password=password,
                phone=phone,
                role=role,
            )
        return user
    

class UserLoginSerializer(serializers.Serializer):

    email = serializers.EmailField(required=True, allow_blank=False)
    password = serializers.CharField(max_length=255, required=True, allow_blank=False)

    def validate(self, attrs):
        email = attrs.get("email", None)
        password = attrs.get("password", None)

        if email is None or password is None:
            raise serializers.ValidationError({"msg": "Email or password missing"})

        try:
            user: User = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError({"msg": "Invalid email or password"})

        if user.check_password(password):
            attrs["user"] = user
        else:
            attrs["user"] = None
            raise serializers.ValidationError({"msg": "Invalid email or password"})

        return attrs

class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs

    def save(self, **kwargs):
        try:
            from rest_framework_simplejwt.tokens import RefreshToken
            RefreshToken(self.token).blacklist()
        except Exception as e:
            self.fail('bad_token')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "first_name", "last_name", "username", "email", "role", "phone")
        read_only_fields = ("id", "role")
