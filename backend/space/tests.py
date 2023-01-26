from rest_framework import status, test
from django.urls import reverse
from space.models import Space


# class SlotBookTests(APITestCase):
#     def test_book_slot_a_day_prior_is_not_valid(self):
#         request = factory.head('/', '', content_type='application/json')
#         view = SlotViewSet.as_view(actions={'patch': 'book_my_slot', })
#         response = view(request)
#         self.assertFalse(False)
#
#     def test_book_slot_a_day_prior_is_valid(self):
#         # reverse(viewname="slot")
#         self.assertTrue(True)

class SpaceViewSetTest(test.APITestCase):
    base_url = reverse(viewname="space-list")

    def setUp(self) -> None:
        for i in range(5):
            Space.objects.create(name=f"Space-{i}")

    def test_space_list(self):
        response = self.client.get(self.base_url)
        self.assertIsInstance(response.data, list)

    def test_space_list_successful_response_code(self):
        response = self.client.get(self.base_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_space_detail_for_valid_id(self):
        space_id = 2
        detail_url = f"{self.base_url}{space_id}/"
        response = self.client.get(path=detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_space_detail_for_invalid_id(self):
        space_id = 10
        detail_url = f"{self.base_url}{space_id}/"
        response = self.client.get(path=detail_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_space_create_no_data(self):
        data = {}
        response = self.client.post(path=self.base_url, data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_space_create_with_existing_name(self):
        data = {"name": "Space-2", "total_slots": 2}
        response = self.client.post(self.base_url, data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_space_create_with_valid_data(self):
        data = {"name": "Space-6", "total_slots": 2}
        count_before_create = Space.objects.count()
        response = self.client.post(self.base_url, data=data)
        count_after_create = Space.objects.count()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(count_after_create, (count_before_create+1))
