from rest_framework import viewsets, status, response, renderers
from rest_framework.decorators import action
from rest_framework.response import Response

from space import serializers, models


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


class SlotViewSet(viewsets.GenericViewSet):
    queryset = models.Slot.objects.all()
    # renderer_classes = [renderers.JSONRenderer, ]

    @action(methods=["PATCH"], detail=True)
    def book_my_slot(self, request, *args, **kwargs):
        data = request.data
        slot = self.get_object()
        serializer = serializers.BookSlotSerializer(instance=slot, data=data)
        if not serializer.is_valid():
            return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        msg = "Successfully Booked Slot!"
        return response.Response({"message": msg}, status=status.HTTP_200_OK)
