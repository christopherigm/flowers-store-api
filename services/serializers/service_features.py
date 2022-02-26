from rest_framework_json_api.serializers import HyperlinkedModelSerializer
from rest_framework_json_api.relations import ResourceRelatedField
from services.models import ServiceFeature

class ServiceFeatureSerializer(HyperlinkedModelSerializer):

    class Meta:
        model=ServiceFeature
        fields="__all__"
