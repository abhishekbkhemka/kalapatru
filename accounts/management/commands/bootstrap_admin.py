from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.conf import settings

from accounts.models import UserProfile


class Command(BaseCommand):
    help = 'Create or update an admin user with the admin role'

    def add_arguments(self, parser):
        parser.add_argument('--username', default='admin')
        parser.add_argument('--password', default='admin123')
        parser.add_argument('--email', default='admin@kalapatru.local')

    def handle(self, *args, **options):
        username = options['username']
        password = options['password']
        email = options['email']

        user, created = User.objects.get_or_create(
            username=username,
            defaults={
                'email': email,
                'is_staff': True,
                'is_superuser': True,
                'is_active': True,
            },
        )
        if not created:
            user.email = email
            user.is_staff = True
            user.is_superuser = True
            user.is_active = True
        user.set_password(password)
        user.save()

        profile, _ = UserProfile.objects.get_or_create(user=user)
        profile.role = settings.ROLE_ADMIN
        profile.is_active_user = True
        profile.save()

        action = 'Created' if created else 'Updated'
        self.stdout.write(self.style.SUCCESS(
            f'{action} admin user "{username}" with role=admin'
        ))
