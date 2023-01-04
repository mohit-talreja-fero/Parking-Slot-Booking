from django.contrib import admin

from .models import Space, Slot, SlotBook


@admin.register(Space)
class SpaceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created')
    list_filter = ('created',)
    search_fields = ('name',)


@admin.register(Slot)
class SlotAdmin(admin.ModelAdmin):
    list_display = ('id', 'space', 'is_available')
    list_filter = ('space', 'is_available')


@admin.register(SlotBook)
class SlotBookAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'slot',
        'duration',
        'start_time',
        'end_time',
        'payment',
    )
    list_filter = ('slot', 'start_time', 'end_time')