import os
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = "Ensure the superuser exists and matches environment variables."

    def handle(self, *args, **options):
        User = get_user_model()

        username = os.getenv("DJANGO_SUPERUSER_USERNAME")
        password = os.getenv("DJANGO_SUPERUSER_PASSWORD")
        email = os.getenv("DJANGO_SUPERUSER_EMAIL", "admin@example.com")

        if not username or not password:
            self.stdout.write(self.style.WARNING(
                "Superuser env vars not set — skipping ensure_superuser."
            ))
            return

        user, created = User.objects.get_or_create(
            username=username,
            defaults={
                "email": email,
                "is_superuser": True,
                "is_staff": True,
            },
        )

        if created:
            user.set_password(password)
            user.save()
            self.stdout.write(self.style.SUCCESS(f"Superuser '{username}' created."))
        else:
            # Ensure flags
            changed = False
            if not user.is_superuser:
                user.is_superuser = True
                changed = True
            if not user.is_staff:
                user.is_staff = True
                changed = True
            if user.email != email:
                user.email = email
                changed = True

            # Always set password from env (allows safe rotation)
            user.set_password(password)
            changed = True

            if changed:
                user.save()
                self.stdout.write(self.style.SUCCESS(f"Superuser '{username}' updated."))
            else:
                self.stdout.write(self.style.SUCCESS(f"Superuser '{username}' unchanged."))
