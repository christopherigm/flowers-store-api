from rest_framework_json_api.serializers import HyperlinkedModelSerializer
from rest_framework_json_api.relations import ResourceRelatedField
from django.contrib.auth.models import User
from users.models import UserFavoriteBuyableItems
from products.models import Product
from services.models import Service

class UserFavoriteBuyableItemsSerializer(HyperlinkedModelSerializer):
    user = ResourceRelatedField (
        queryset = User.objects,
        required = True
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
        model = UserFavoriteBuyableItems
        fields = "__all__"
        extra_kwargs = {
            "created": {
                "read_only": True
            },
            "modified": {
                "read_only": True
            }
        }
