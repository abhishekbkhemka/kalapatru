from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.conf import settings
from django.db import connection

from accounts.models import UserProfile
from LR.models import Organization


class Command(BaseCommand):
    help = 'Bootstrap local admin user and default organization (safe for empty local DB)'

    def add_arguments(self, parser):
        parser.add_argument(
            '--username',
            default=None,
            help='Admin username (default: BOOTSTRAP_ADMIN_USER or admin)',
        )
        parser.add_argument(
            '--password',
            default=None,
            help='Admin password (default: BOOTSTRAP_ADMIN_PASSWORD or admin123)',
        )

    def handle(self, *args, **options):
        import os

        username = options['username'] or os.environ.get('BOOTSTRAP_ADMIN_USER', 'admin')
        password = options['password'] or os.environ.get('BOOTSTRAP_ADMIN_PASSWORD', 'admin123')

        user, created = User.objects.get_or_create(
            username=username,
            defaults={
                'email': f'{username}@localhost',
                'is_staff': True,
                'is_superuser': True,
                'is_active': True,
            },
        )
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.set_password(password)
        user.save()

        profile, _ = UserProfile.objects.get_or_create(user=user)
        profile.role = settings.ROLE_ADMIN
        profile.is_active_user = True
        profile.save()

        org, org_created = Organization.objects.get_or_create(
            id=1,
            defaults={'name': 'Kalapatru Local'},
        )
        if org_created or not org.name:
            org.name = org.name or 'Kalapatru Local'
            org.save()
        org.user.add(user)

        # Ensure autoincrement won't collide if we forced id=1
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT COALESCE(MAX(id), 1) FROM LR_organization"
            )
            max_id = cursor.fetchone()[0]
            try:
                cursor.execute(
                    "ALTER TABLE LR_organization AUTO_INCREMENT = %s",
                    [max_id + 1],
                )
            except Exception:
                pass

        action = 'Created' if created else 'Updated'
        self.stdout.write(self.style.SUCCESS(
            f'{action} admin "{username}" / role=admin; org_id={org.id}'
        ))
        self.stdout.write(self.style.SUCCESS(
            f'Login with username={username} password={password}'
        ))
