from django.urls import reverse

from rest_framework import status, test
from space.models import Slot, Space


class SlotViewSetTest(test.APITestCase):
    space_url = reverse(viewname="space-list")
    slot_url = reverse(viewname="space-list")

    def setUp(self) -> None:
        for i in range(5):
            Space.objects.create(name=f"Space-{i}")

    def test_slot_unavailable_by_default(self):
        unavailable_slot_count = Slot.objects.filter(is_available=False).count()
        self.assertEqual(unavailable_slot_count, 0)

    def test_slot_created_count(self):
        total_slots = 4
        data = {"name": "Space-6", "total_slots": total_slots}
        response = self.client.post(self.space_url, data=data)

        created_slots_count = Slot.objects.filter(space=response.data.get('id')).count()
        self.assertEqual(total_slots, created_slots_count)
