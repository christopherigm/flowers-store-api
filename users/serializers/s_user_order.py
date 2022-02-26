from rest_framework_json_api.serializers import HyperlinkedModelSerializer
from rest_framework_json_api.relations import ResourceRelatedField
from django.contrib.auth.models import User
from users.models import UserOrderBuyableItem, UserOrder
from products.models import Product
from services.models import Service

class UserOrderBuyableItemSerializer(HyperlinkedModelSerializer):
    user = ResourceRelatedField (
        queryset = User.objects,
        required = True
    )
    purchase_order = ResourceRelatedField (
        queryset = UserOrder.objects,
        required=False,
        allow_null=True
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
        model = UserOrderBuyableItem
        fields = "__all__"
        extra_kwargs = {
            "created": {
                "read_only": True
            },
            "modified": {
                "read_only": True
            }
        }


class UserOrderSerializer(HyperlinkedModelSerializer):
    user = ResourceRelatedField (
        queryset = User.objects,
        required = True
    )
    order_items = ResourceRelatedField (
        queryset = UserOrderBuyableItem.objects,
        required = False,
        many=True
    )

    included_serializers = {
        "user": "users.serializers.UserSerializer",
        "order_items": "users.serializers.UserOrderBuyableItemSerializer"
    }

    class Meta:
        model = UserOrder
        fields = "__all__"
        extra_kwargs = {
            "created": {
                "read_only": True
            },
            "modified": {
                "read_only": True
            }
        }
