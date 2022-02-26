from rest_framework_json_api.serializers import HyperlinkedModelSerializer
from rest_framework_json_api.relations import ResourceRelatedField
from services.models import ServiceClassification

class ServiceClassificationSerializer(HyperlinkedModelSerializer):

    class Meta:
        model=ServiceClassification
        fields="__all__"
