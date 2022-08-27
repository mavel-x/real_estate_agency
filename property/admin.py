from django.contrib import admin

from .models import Complaint, Flat, Owner


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address', 'owner', 'pk')
    readonly_fields = ('created_at',)
    list_display = (
        'address',
        'price',
        'new_building',
        'construction_year',
        'town',
        'owner',
        'owners_phonenumber',
        'owner_pure_phone',
    )
    list_editable = ('new_building',)
    list_filter = ('new_building', 'rooms_number', 'has_balcony')
    raw_id_fields = ('liked_by',)


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('user', 'flat')


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    search_fields = ('normalized_phone', 'name', 'pk')
    raw_id_fields = ('flats',)
    list_display = (
        'name',
        'normalized_phone',
    )
