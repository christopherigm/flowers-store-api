from django.db import models
from django.contrib.auth.models import User
from common.models import (
    Address,
    City
)

class UserAddress(Address):
    user = models.ForeignKey (
        User,
        null = False,
        blank = False,
        on_delete = models.CASCADE
    )
    city = models.ForeignKey (
        City,
        related_name = 'user_city_address',
        null = True,
        blank = True,
        on_delete = models.CASCADE
    )

    def __str__(self):
        return self.alias

    class Meta:
        verbose_name = "User address"
        verbose_name_plural = "User address'"

    class JSONAPIMeta:
        resource_name = "UserAddress"
