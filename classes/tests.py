from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

# Create your tests here.


class ClassTest(APITestCase):
    def setUp(self):
        self.user_data = {"username": "testuser", "password": "testpassword"}
        self.class_data = {"title": "test class title", "category": "programming",
                           "content": "test class content", "thumbnail": ""}
        self.user = User.objects.create_user(
            username="testuser", password="testpassword", email="test@gmail.com")
        self.token = Token.objects.create(user=self.user)

    # 로그인을 안한 상태에서의 수업 생성 테스트
    def test_create_class_not_login(self):
        url = '/classes/'
        response = self.client.post(url, self.class_data)
        self.assertEqual(response.status_code, 401)

    # 로그인을 한 상태에서의 수업 생성 테스트
    def test_create_class_login(self):
        url = '/classes/'
        response = self.client.post(
            url, self.class_data, HTTP_AUTHORIZATION="Token " + str(self.token))
        self.assertEqual(response.status_code, 201)
