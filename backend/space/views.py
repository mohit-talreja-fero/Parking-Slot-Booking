from rest_framework import viewsets, status, response
from rest_framework.decorators import action

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


class SlotViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.BookSlotSerializer
    queryset = models.Slot.objects.all()

    @action(methods=["POST"], detail=True)
    def book_my_slot(self, request, *args, **kwargs):
        data = request.data
        slot = self.get_object()
        serializer = serializers.BookSlotSerializer(instance=slot, data=data)
        if not serializer.is_valid():
            return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return response.Response(serializer.data, status=status.HTTP_200_OK)
