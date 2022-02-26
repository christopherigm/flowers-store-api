from rest_framework_json_api.serializers import HyperlinkedModelSerializer
from rest_framework_json_api.relations import ResourceRelatedField
from django.contrib.auth.models import User
from users.models import UserCartBuyableItems
from products.models import Product
from services.models import Service

class UserCartBuyableItemsSerializer(HyperlinkedModelSerializer):
    user = ResourceRelatedField (
        queryset = User.objects
    )
    product = ResourceRelatedField (
        queryset = Product.objects,
        required=False,
        allow_null=True
    )
    service = ResourceRelatedField (
        queryset = Service.objects,
        required=False,
        allow_null=True
    )

    included_serializers = {
        "user": "users.serializers.UserSerializer",
        "product": "products.serializers.ProductSerializer",
        "service": "services.serializers.ServiceSerializer"
    }

    class Meta:
        model = UserCartBuyableItems
        fields = "__all__"
        extra_kwargs = {
            "created": {
                "read_only": True
            },
            "modified": {
                "read_only": True
            }
        }
