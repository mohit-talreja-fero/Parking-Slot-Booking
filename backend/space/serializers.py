from rest_framework import serializers
from .models import Slot, Space, SlotBook


class SpaceListSerializer(serializers.ModelSerializer):
    total_slots = serializers.SerializerMethodField()

    class Meta:
        model = Space
        fields = (
            "id", "name", "total_slots",
        )

    def get_total_slots(self, space: Space):
        return space.space_slots.count()

    def get_available_slots(self, space: Space):
        return space.space_slots.filter(is_available=True).count()

    def get_occupied_slots(self, space: Space):
        return space.space_slots.filter(is_available=False).count()


class SpaceDetailSerializer(SpaceListSerializer):
    available_slots = serializers.SerializerMethodField()
    occupied_slots = serializers.SerializerMethodField()

    class Meta:
        model = Space
        fields = (
            "id", "name", "total_slots", "available_slots", "occupied_slots",
        )

    def get_available_slots(self, space: Space):
        return space.space_slots.filter(is_available=True).count()

    def get_occupied_slots(self, space: Space):
        return space.space_slots.filter(is_available=False).count()


class SpaceSerializer(serializers.ModelSerializer):
    total_slots = serializers.IntegerField(
        min_value=1, write_only=True, required=True,
        error_messages={"min_value": "Space should have at least 1 slot"}
    )
    name = serializers.CharField()

    class Meta:
        model = Space
        fields = (
            "id", "name", "total_slots",
        )

    def validate(self, attrs):
        name = attrs.get("name", self.instance.name)
        if self.instance:
            attrs["name"] = self.instance.name
        else:
            if Space.objects.filter(name__iexact=name).exists():
                raise serializers.ValidationError({"name": f"Space with Name {name} already exists"})
        return attrs

    def create(self, validated_data: dict):
        total_slots = validated_data.pop("total_slots")
        space = super(SpaceSerializer, self).create(validated_data=validated_data)
        space.add_slots(total_slots=total_slots)
        return space

    def update(self, instance, validated_data):
        total_slots = validated_data.pop("total_slots")
        space = super(SpaceSerializer, self).update(instance, validated_data)
        space.add_slots(total_slots=total_slots)
        return space
