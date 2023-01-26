from django.utils import timezone
from rest_framework import serializers
from lib import constants
from .helpers import get_duration_and_payment_for_start_and_end_time
from .models import Slot, Space


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

    def validate_name(self, name):
        if Space.objects.filter(name__iexact=name).exists():
            raise serializers.ValidationError({"name": f"Space with Name {name} already exists"})
        return name

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


class SLotListSerializer(serializers.ModelSerializer):
    space_name = serializers.CharField(source="space.name")

    class Meta:
        model = Slot
        fields = ("id", "space_id", "space_name", "is_available")


class BookSlotSerializer(serializers.ModelSerializer):
    start_time = serializers.DateTimeField(
        format=constants.GeneralConstants.DATE_TIME_FORMAT, write_only=True, required=True)
    end_time = serializers.DateTimeField(
        format=constants.GeneralConstants.DATE_TIME_FORMAT, write_only=True, required=True)
    payment = serializers.IntegerField(min_value=1, required=True, write_only=True)
    duration = serializers.IntegerField(required=False, write_only=True)

    class Meta:
        model = Slot
        fields = ("id", "start_time", "end_time", "payment", "duration",)

    def validate_start_time(self, start_time):
        if start_time < timezone.now():
            raise serializers.ValidationError("Past date mat bhej bhai samaj nahi aata kya")

        time_difference = start_time - timezone.now()
        if time_difference.days != 1:
            raise serializers.ValidationError("Slot should be booked 24 Hrs prior")
        return start_time

    def validate(self, attrs):
        slot = self.instance

        start_time = attrs.get("start_time")
        end_time = attrs.get("end_time")
        duration = attrs.get("duration")  # Calculate on frontend to display user
        payment = attrs.get("payment")

        if start_time >= end_time:
            raise serializers.ValidationError("End Time should be greater than Start Time")

        if not duration:
            duration = end_time - start_time

        if not slot.is_available:
            raise serializers.ValidationError({"id": f"Slot is not available"})

        attrs["is_available"] = False
        return attrs

    def update(self, instance, validated_data: dict):
        details = {
            "start_time": validated_data.pop("start_time"),
            "end_time": validated_data.pop("end_time"),
        }

        duration, payment = get_duration_and_payment_for_start_and_end_time(
            start_time=details["start_time"], end_time=details["end_time"])
        details.update({
            "payment": payment,
            "duration": duration,
        })
        slot = super(BookSlotSerializer, self).update(instance=instance, validated_data=validated_data)
        slot.book_slot(details=details)
        return slot
