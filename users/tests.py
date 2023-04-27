from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

# Create your tests here.
# 회원가입 테스트


class UserRegisterAPITestCase(APITestCase):
    def test_registration(self):
        url = reverse('register_view')
        user_data = {
            "username": "testusername",
            "password": "testpassword",
            "password2": "testpassword",
            "email": "test@gmail.com",
        }
        response = self.client.post(url, user_data)
        # 회원가입 진행 후의 상태 코드가 201인지 확인
        self.assertEqual(response.status_code, 201)
