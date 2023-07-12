from rest_framework.test import APITestCase, APIRequestFactory

# from .views import PostListCreateView
from django.urls import reverse
from rest_framework import status


class CreateDeviceTestCase(APITestCase):
    def test_valid_request_test(self):
        valid_request = {
            "id": "/devices/id5",
            "deviceModel": "/devicemodels/id5",
            "name": "Sensor5",
            "note": "Testing a sensor5.",
            "serial": "A020000105",
        }
        response = self.client.post(reverse("device_store"), valid_request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["message"], "Device created successfully")

    def test_invalidRequest(self):
        # -- all attributes are required . this is a test for that --#
        invalid_request = {
            "id": "/devices/id5",
            "note": "Testing a sensor5.",
            "serial": "A020000105",
        }
        response = self.client.post(reverse("device_store"), invalid_request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_invalidId(self):
        # -- if id is not in required format our app raises error (required format:/devices/id<id>) --#
        invalid_request = {
            "id": "id5",  # wrong format
            "deviceModel": "/devicemodels/id5",
            "name": "Sensor5",
            "note": "Testing a sensor5.",
            "serial": "A020000105",
        }
        response = self.client.post(reverse("device_store"), invalid_request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class ShowDeviceTest(APITestCase):
    def test_show_valid_request(self):
        response = self.client.get(reverse("device_show", kwargs={"id": 2}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_non_existing_device(self):
        response = self.client.get(reverse("device_show", kwargs={"id": 15}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data["error"], "device Not Found")
