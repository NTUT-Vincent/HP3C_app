from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from rest_framework.utils import json

from high_value_computer import settings
from user_management.models import User


class UserViewTestCase(APITestCase):
    url = '/api/user/'
    detail_url = '/api/user/{}'
    databases = settings.DATABASES

    def setUp(self):
        self.client = APIClient()
        self.user_init = {
            "user_id": 'user0001',
            "name": 'User01',
            "password": 'pw123456',
            "gender": 'M',
            "address": 'TW, KH',
            "user_type": 3
        }
        self.user = User.objects.create(
            user_id='user0001', name='test_user01', password='pw123456', gender='M', address='TW, KH', user_type=3)

    def test_api_user_get(self):
        expected_data = [{
            "user_id": 'user0001',
            "name": 'test_user01',
            "password": 'pw123456',
            "gender": 'M', "address": 'TW, KH',
            "user_type": 3
        }]
        response = self.client.get(
            self.url,
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(json.loads(response.content), expected_data)

    def test_api_user_create_success(self):
        request_data = {
            "user_id": 'user0002',
            "name": 'User02',
            'password': 'pwd00002',
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
        self.assertEqual(json.loads(response.content), request_data)

    def test_api_user_create_duplicate(self):
        request_data = {
            "user_id": 'user0001',
            "name": 'test_user02',
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

    def test_user_detail_get_success(self):
        user_id = 'user0001'
        expected_data = {
            "user_id": 'user0001',
            "name": 'test_user01',
            "password": 'pw123456',
            "gender": 'M',
            "address": 'TW, KH',
            "user_type": 3
        }
        response = self.client.get(
            self.detail_url.format(user_id),
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(json.loads(response.content), expected_data)

    def test_user_detail_update_success(self):
        user_id = 'user0001'
        request_data = {
            "user_id": "user0001",
            "name": "User21",
            "password": "pwd000021",
            "gender": "M",
            "address": "TW, KH",
            "user_type": 3
        }
        response = self.client.put(
            self.detail_url.format(user_id),
            request_data,
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(json.loads(response.content), request_data)
