from django.contrib.auth.models import AbstractUser


class SystemUsers(AbstractUser):
    pass

    def __str__(self):
        return self.username
