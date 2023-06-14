"""File to autocreate a superuser automatically."""
from django.db import IntegrityError
from django.contrib.auth.models import User

try:
    superuser = User.objects.create_superuser(
        username="superadmin",
        email="superadmin@email.com",
        password="superpassword")
    superuser.save()
except IntegrityError:
    print(f"Super User with username superadmin is already exists!")
except Exception as e:
    print(e)
