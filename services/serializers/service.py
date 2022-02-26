from rest_framework_json_api.serializers import HyperlinkedModelSerializer
from rest_framework_json_api.relations import ResourceRelatedField
from services.models import (
    Service,
    ServiceClassification,
    ServiceFeature,
    ServicePicture
)

class ServiceSerializer(HyperlinkedModelSerializer):

    classification=ResourceRelatedField( queryset=ServiceClassification.objects )
    features=ResourceRelatedField(
        queryset=ServiceFeature.objects,
        many=True
    )
    service_pictures=ResourceRelatedField(
        queryset=ServicePicture.objects,
        many=True
    )
    related=ResourceRelatedField(
        queryset=Service.objects,
        many=True
    )

    included_serializers={
        "classification": "services.serializers.ServiceClassificationSerializer",
        "features": "services.serializers.ServiceFeatureSerializer",
        "service_pictures": "services.serializers.ServicePictureSerializer",
        "related": "services.serializers.ServiceSerializer"
    }

    class Meta:
        model=Service
        fields="__all__"
