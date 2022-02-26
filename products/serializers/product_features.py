from rest_framework_json_api.serializers import HyperlinkedModelSerializer
from rest_framework_json_api.relations import ResourceRelatedField
from products.models import (
    ProductFeature,
    ProductFeatureOption
)

class ProductFeatureOptionSerializer(HyperlinkedModelSerializer):
    feature=ResourceRelatedField( queryset=ProductFeature.objects )

    class Meta:
        model=ProductFeatureOption
        fields="__all__"


class ProductFeatureSerializer(HyperlinkedModelSerializer):
    options=ResourceRelatedField( queryset=ProductFeatureOption.objects )

    included_serializers = {
        "options": "products.serializers.ProductFeatureOptionSerializer"
    }

    class Meta:
        model=ProductFeature
        fields="__all__"
