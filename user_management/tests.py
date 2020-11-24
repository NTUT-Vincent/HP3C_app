from django.test import TestCase

# Create your tests here.
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from high_value_computer import settings
from user_management.models import User


class UserViewTestCase(APITestCase):
    url = '/api/user/'
    url_detail = '/api/user/id/{}/'
    databases = settings.DATABASES

    def setUp(self):
        self.client = APIClient()

        self.user = User.objects.create(
            user_id='user0001', name='test_user01', password='pw123456', gender='M', address='TW, KH', user_type=3)

    def test_api_user_get(self):
        user_id = 'user0001'
        response = self.client.get(
            self.url,
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get(pk=user_id).user_id, 'user0001')
        self.assertEqual(User.objects.get(pk=user_id).name, 'test_user01')

    def test_api_user_create_success(self):
        request_data = {
            "user_id": 'user0002',
            "name": 'test_user02',
            'password': 'pw0002',
            "gender": 'M',
            "address": 'TW, KH',
            "user_type": 3
        }
        response = self.client.post(
            self.url,
            request_data,
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)
        self.assertEqual(User.objects.get(pk=request_data.get('user_id')).user_id, 'user0002')
        self.assertEqual(User.objects.get(pk=request_data.get('user_id')).name, 'test_user02')

    def test_api_user_create_duplicate(self):
        request_data = {
            "user_id": 'user0001',
            "name": 'test_user01',
            'password': 'pw0001',
            "gender": 'M',
            "address": 'TW, KH',
            "user_type": 3
        }
        response = self.client.post(
            self.url,
            request_data,
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get(pk=request_data.get('user_id')).user_id, 'user0001')
        self.assertEqual(User.objects.get(pk=request_data.get('user_id')).name, 'test_user01')

    def test_user_update_success(self):
        request_data = {
            "user_id": "user0001",
            "name": "test_user21",
            "password": "pw0021",
            "gender": "M",
            "address": "TW, KH",
            "user_type": 4
        }
        user_id = 'user0001'
        response = self.client.put(
            self.url_detail.format(user_id),
            request_data,
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get(pk=request_data.get('user_id')).user_id, 'user0001')
        self.assertEqual(User.objects.get(pk=request_data.get('user_id')).name, 'test_user21')

    def test_user_delete_success(self):
        user_id = 'user0001'
        response = self.client.delete(
            self.url_detail.format(user_id),
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(User.objects.count(), 0)

    # def test_user_
