from rest_framework import serializers
from .models import Slot, Space, SlotBook


class SpaceListSerializer(serializers.ModelSerializer):
    # total_slots = serializers.SerializerMethodField()

    class Meta:
        model = Space
        fields = (
            "id", "name", "total_slots",
        )


class SpaceDetailSerializer(SpaceListSerializer):
    # available_slots = serializers.SerializerMethodField()
    # occupied_slots = serializers.SerializerMethodField()

    class Meta:
        model = Space
        fields = (
            "id", "name", "total_slots", "unoccupied_slots", "occupied_slots",
        )


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


class BookSlotSerializer(serializers.ModelSerializer):
    start_time = serializers.DateTimeField(write_only=True, required=True)
    end_time = serializers.DateTimeField(write_only=True, required=True)
    payment = serializers.IntegerField(min_value=1, required=True)
    duration = serializers.IntegerField(required=False, write_only=True)

    class Meta:
        model = Slot
        fields = ("id",)

    def validate(self, attrs):
        slot_id = attrs.get("id")
        start_time = attrs.get("start_time")
        end_time = attrs.get("end_time")
        duration = attrs.get("duration")  # Calculate on frontend to display user
        payment = attrs.get("payment")

        if start_time >= end_time:
            raise serializers.ValidationError("End Time should be greater than Start Time")

        if not duration:
            duration = end_time - start_time

        try:
            slot = Slot.objects.get(id=slot_id)
        except Slot.DoesNotExist:
            raise serializers.ValidationError({"id": f"Slot with ID {slot_id} does not exists"})
        else:
            if not slot.is_available:
                raise serializers.ValidationError({"id": f"Slot with ID {slot_id} is not available"})

        attrs["is_available"] = False
        return attrs

    def update(self, instance, validated_data: dict):
        details = {
            "start_time": validated_data.pop("start_time"),
            "end_time": validated_data.pop("end_time"),
        }
        slot = super(BookSlotSerializer, self).update(instance=instance, validated_data=validated_data)
        slot.book_slot(details=details)
        return slot
