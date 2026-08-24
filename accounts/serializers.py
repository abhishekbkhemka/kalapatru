from django.contrib.auth.models import User
from django.conf import settings
from rest_framework import serializers

from .models import UserProfile


class UserSerializer(serializers.ModelSerializer):
    role = serializers.SerializerMethodField()
    is_active_user = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'is_active',
            'role',
            'is_active_user',
            'date_joined',
            'last_login',
        )
        read_only_fields = fields

    def get_role(self, obj):
        if obj.is_superuser:
            return settings.ROLE_ADMIN
        profile = getattr(obj, 'profile', None)
        return profile.role if profile else settings.ROLE_VIEWER

    def get_is_active_user(self, obj):
        profile = getattr(obj, 'profile', None)
        if profile is None:
            return obj.is_active
        return profile.is_active_user and obj.is_active


class UserCreateUpdateSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(write_only=True, required=False, allow_blank=False, min_length=6)
    email = serializers.EmailField(required=False, allow_blank=True, default='')
    first_name = serializers.CharField(required=False, allow_blank=True, default='')
    last_name = serializers.CharField(required=False, allow_blank=True, default='')
    role = serializers.ChoiceField(choices=UserProfile.ROLE_CHOICES)
    is_active = serializers.BooleanField(default=True)

    def validate_username(self, value):
        qs = User.objects.filter(username=value)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError('Username already taken.')
        return value

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        if not password:
            raise serializers.ValidationError({'password': 'Password is required.'})
        role = validated_data.pop('role')
        is_active = validated_data.pop('is_active', True)
        user = User(**validated_data)
        user.is_active = is_active
        user.set_password(password)
        if role == settings.ROLE_ADMIN:
            user.is_staff = True
        user.save()
        profile, _ = UserProfile.objects.get_or_create(user=user)
        profile.role = role
        profile.is_active_user = is_active
        profile.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        role = validated_data.pop('role', None)
        is_active = validated_data.pop('is_active', None)

        for field in ('username', 'email', 'first_name', 'last_name'):
            if field in validated_data:
                setattr(instance, field, validated_data[field])

        if is_active is not None:
            instance.is_active = is_active

        if password:
            instance.set_password(password)

        if role is not None:
            instance.is_staff = role == settings.ROLE_ADMIN
            profile, _ = UserProfile.objects.get_or_create(user=instance)
            profile.role = role
            if is_active is not None:
                profile.is_active_user = is_active
            profile.save()
        elif is_active is not None:
            profile, _ = UserProfile.objects.get_or_create(user=instance)
            profile.is_active_user = is_active
            profile.save()

        instance.save()
        return instance
