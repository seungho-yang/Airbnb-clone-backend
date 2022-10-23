from django.contrib import admin
from .models import House


@admin.register(House)
class HouseAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "price",
        "address",
        "pets_allowed",
    )
    list_filter = ("price", "pets_allowed")
    search_fields = ("address", )
    list_display_links = ("name", "address")
    list_editable = ("pets_allowed", )

