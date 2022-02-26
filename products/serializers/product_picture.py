from rest_framework_json_api.serializers import HyperlinkedModelSerializer
from rest_framework_json_api.relations import ResourceRelatedField
from products.models import ProductPicture
from products.models import Product

class ProductPictureSerializer(HyperlinkedModelSerializer):
    product=ResourceRelatedField( queryset=Product.objects )

    class Meta:
        model=ProductPicture
        fields="__all__"
