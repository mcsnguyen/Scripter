from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Subscription?
    # User profiles?
    # anything else?

    def __str__(self):
        return f'{self.user.username}'


