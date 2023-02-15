from django_filters import rest_framework as filters

from space import models


class SlotAvailabilityFilter(filters.FilterSet):
    start_time = filters.TimeFilter(method="start_time__gt")

    class Meta:
        model = models.Slot
        fields = ("start_time",)

    def start_time__gt(self, queryset, name, value):
        return queryset
