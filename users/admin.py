from django.contrib import admin
from users.models import (
    UserAddress,
    UserProfile,
    UserCartBuyableItems,
    UserFavoriteBuyableItems,
    UserOrderBuyableItem,
    UserOrder
)

# Register your models here.

class UserAddressAdmin(admin.ModelAdmin):
    list_display = [
        "alias",
        "city",
        "enabled"
    ]
    search_fields = ("alias",)
    list_filter = ("enabled", "city")
    readonly_fields=(
        "version",
    )
admin.site.register(UserAddress, UserAddressAdmin)

class UserProfileAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "owner_position"
    ]
    readonly_fields=(
        "version",
        "order"
    )
    readonly_fields=(
        "version",
    )
admin.site.register(UserProfile, UserProfileAdmin)

class UserCartBuyableItemsAdmin(admin.ModelAdmin):
    list_display = [
        "backup_name",
        "user",
        "quantity",
        "product",
        "service"
    ]
    search_fields = ("backup_name", "backup_user_name")
    list_filter = (
        "enabled",
        "user",
        "product",
        "service"
    )
    readonly_fields=(
        "version",
        "backup_name",
        "backup_user_name",
        "backup_final_price"
    )
admin.site.register(UserCartBuyableItems, UserCartBuyableItemsAdmin)

class UserFavoriteBuyableItemsAdmin(admin.ModelAdmin):
    list_display = [
        "backup_name",
        "user",
        "product",
        "service"
    ]
    search_fields = ("backup_name", "backup_user_name")
    list_filter = (
        "enabled",
        "user",
        "product",
        "service"
    )
    readonly_fields=(
        "version",
        "backup_name",
        "backup_user_name",
        "backup_final_price"
    )
admin.site.register(UserFavoriteBuyableItems, UserFavoriteBuyableItemsAdmin)

class UserOrderBuyableItemAdmin(admin.ModelAdmin):
    list_display = [
        "backup_name",
        "user",
        "quantity",
        "product",
        "service"
    ]
    search_fields = ("backup_name", "backup_user_name")
    list_filter = (
        "enabled",
        "user",
        "product",
        "service"
    )
    readonly_fields=(
        "version",
        "backup_name",
        "backup_user_name",
        "backup_final_price"
    )
admin.site.register(UserOrderBuyableItem, UserOrderBuyableItemAdmin)

class UserOrderAdmin(admin.ModelAdmin):
    list_display = [
        "broker_id",
        "user",
        "receptor_name",
        "phone"
    ]
    search_fields = ("broker_id", "address", "receptor_name")
    list_filter = (
        "enabled", "user", "broker_id"
    )
    readonly_fields=(
        "version",
        "backup_user_name",
    )
admin.site.register(UserOrder, UserOrderAdmin)
