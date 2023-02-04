from django.urls import reverse
from django.contrib.auth.models import User

from rest_framework import status, test


class LoginViewTest(test.APITestCase):
    login_url = reverse(viewname="login")

    def setUp(self):
        User.objects.create_user(username="user1", password="fero@1234")

    def test_login_with_valid_credentials(self):
        data = {"username": "user1", "password": "fero@1234"}
        response = self.client.post(path=self.login_url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Check if returned response has "token" in it or not
        self.assertTrue("token" in response.data.keys(), msg="Token returned from Login API")

    def test_login_without_credentials(self):
        data = {}
        response = self.client.post(path=self.login_url, data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_login_with_invalid_credentials(self):
        data = {"username": "user1", "password": "wrong_password"}
        response = self.client.post(path=self.login_url, data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
