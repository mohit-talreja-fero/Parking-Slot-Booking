from django.db.models import Count, Q, Case, When
from rest_framework import viewsets, status, response, renderers, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from space import serializers, models, filters


class SpaceViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.SpaceListSerializer
    queryset = models.Space.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return serializers.SpaceListSerializer
        if self.action in ["create", "update", "partial_update"]:
            return serializers.SpaceSerializer

        return serializers.SpaceDetailSerializer

    @action(methods=["GET"], detail=True)
    def slot_list(self, request, *args, **kwargs):
        space = self.get_object()
        space_slots = space.space_slots.all()
        serializer = serializers.SLotListSerializer(space_slots, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SlotViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin):
    queryset = models.Slot.objects.all()
    serializer_class = serializers.SLotListSerializer

    def get_serializer_context(self):
        context = super(SlotViewSet, self).get_serializer_context()
        context["user"] = self.request.user
        return context

    @action(methods=["PATCH"], detail=True)
    def book_my_slot(self, request, *args, **kwargs):
        data = request.data
        slot = self.get_object()
        context = {"user": self.request.user}
        serializer = serializers.BookSlotSerializer(instance=slot, data=data, context=context)
        if not serializer.is_valid():
            return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        msg = "Successfully Booked Slot!"
        return response.Response({"message": msg}, status=status.HTTP_200_OK)

    @action(methods=["GET"], detail=False)
    def show_available_slots(self, request, *args, **kwargs):
        start_time = request.query_params.get("start_time")
        end_time = request.query_params.get("end_time")
        if not (start_time and end_time):
            return Response({
                "non_field_errors": "Please Provide Start Time and End Time"
            }, status=status.HTTP_400_BAD_REQUEST)

        if start_time >= end_time:
            return Response({"errors": {
                "start_time": "Start Time should be less than End Time"
            }}, status=status.HTTP_400_BAD_REQUEST)

        slots = models.Slot.objects.prefetch_related(
            "slot_bookings").annotate(
            availability=Case(When(
                Q(slot_bookings__start_time__gte=start_time) &
                Q(slot_bookings__end_time__lte=end_time),
                then=False
            ), default=True)
        ).distinct()
        serializer = serializers.SlotAvailabilitySerializer(slots, many=True)
        return Response(serializer.data)
