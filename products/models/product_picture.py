from django.db import models
from common.models import MediumPicture

class ProductPicture(MediumPicture):
    product=models.ForeignKey(
        "products.Product",
        verbose_name="Producto",
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )

    def __str__(self):
        name=self.name or 'picture'
        return "{} - {}".format(
            self.product.name,
            name
        )

    class Meta:
        verbose_name="Foto del producto"
        verbose_name_plural="Fotos de los productos"

    class JSONAPIMeta:
        resource_name="ProductPicture"
