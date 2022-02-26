from django.db import models
from common.models import CommonFields

class ServiceFeature(CommonFields):
    name=models.CharField (
        max_length=64,
        null=False,
        blank=False,
        unique=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name="Caracteristica del servicio"
        verbose_name_plural="Caracteristicas de los servicios"

    class JSONAPIMeta:
        resource_name="ServiceFeature"
