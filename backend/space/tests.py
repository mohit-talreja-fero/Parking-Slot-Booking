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
