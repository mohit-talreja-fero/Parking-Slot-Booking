from rest_framework import viewsets
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
