"""flowers_store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include
from rest_framework import routers, permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from common.views import (
    CountryViewSet,
    StateViewSet,
    CityViewSet,
    System,
    SprintViewSet,
    ChangeLogViewSet,
    SystemViewSet,
    HomePictureViewSet
)
from users.views import (
    UserViewSet,
    GroupViewSet,
    UserAddressViewSet,
    UserCartBuyableItemsViewSet,
    UserFavoriteBuyableItemsViewSet,
    UserOrderBuyableItemViewSet,
    UserOrderViewSet,
    UserProfileViewSet,
    Login,
    ActivateUser
)
from products.views import (
    ProductClassificationViewSet,
    ProductDeliveryTypeViewSet,
    ProductFeatureViewSet,
    ProductFeatureOptionViewSet,
    ProductPictureViewSet,
    ProductViewSet
)
from services.views import (
    ServiceClassificationViewSet,
    ServiceFeatureViewSet,
    ServicePictureViewSet,
    ServiceViewSet
)

router=routers.DefaultRouter()

router.register(r'system', SystemViewSet)
router.register(r'home-pictures', HomePictureViewSet)

router.register(r'users', UserViewSet)
router.register(r'user-address', UserAddressViewSet)
router.register(r'user-profile', UserProfileViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'user-cart-items', UserCartBuyableItemsViewSet)
router.register(r'user-favorite-items', UserFavoriteBuyableItemsViewSet)
router.register(r'user-order-items', UserOrderBuyableItemViewSet)
router.register(r'user-orders', UserOrderViewSet)

router.register(r'countries', CountryViewSet)
router.register(r'states', StateViewSet)
router.register(r'cities', CityViewSet)
router.register(r'sprints', SprintViewSet)
router.register(r'changelogs', ChangeLogViewSet)

router.register(r'product-classifications', ProductClassificationViewSet)
router.register(r'product-delivery-types', ProductDeliveryTypeViewSet)
router.register(r'product-features', ProductFeatureViewSet)
router.register(r'product-feature-options', ProductFeatureOptionViewSet)
router.register(r'product-images', ProductPictureViewSet)
router.register(r'products', ProductViewSet)

router.register(r'services-classifications', ServiceClassificationViewSet)
router.register(r'services-features', ServiceFeatureViewSet)
router.register(r'services-pictures', ServicePictureViewSet)
router.register(r'services', ServiceViewSet)

# https://github.com/axnsan12/drf-yasg
schema_view=get_schema_view(
    openapi.Info(
        title='API Docs',
        default_version='v1',
        # description='',
        # terms_of_service='',
        contact=openapi.Contact(email='christopher.guzman.monsalvo@gmail.com'),
        license=openapi.License(name='GPL License'),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns=[
    path('jet/', include('jet.urls', 'jet')),
    path('admin/', admin.site.urls),
    re_path(r'^v1/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    re_path(r'^v1/token/$', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    re_path(r'^v1/token/refresh/$', TokenRefreshView.as_view(), name='token_refresh'),
    re_path(r'^v1/token/verify/$', TokenVerifyView.as_view(), name='token_verify'),
    re_path(r'^v1/login', Login.as_view(), name='login'),
    re_path(r'^v1/activate-user', ActivateUser.as_view(), name='login'),
    path('tinymce/', include('tinymce.urls')),
    path('v1/system/info', System.as_view()),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

