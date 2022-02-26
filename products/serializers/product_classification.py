from rest_framework_json_api.serializers import HyperlinkedModelSerializer
from rest_framework_json_api.relations import ResourceRelatedField
from products.models import ProductClassification

class ProductClassificationSerializer(HyperlinkedModelSerializer):

    class Meta:
        model=ProductClassification
        fields="__all__"
