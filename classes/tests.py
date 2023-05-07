from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import Class
from users.models import Profile

# Create your tests here.

# 수업 생성 테스트


class ClassCreateTest(APITestCase):
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


# 수업 조회 테스트
class ClassGetTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="testpassword", email="test@gmail.com")
        self.cls = Class.objects.create(instructor=self.user, profile=Profile.objects.get(
            user=self.user), title="test title", category="test category", content="test content", thumbnail="")

    def test_read_class(self):
        pk = self.cls.id
        url = '/classes/' + str(pk) + '/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


# 수업 삭제 테스트
class ClassDeleteTest(APITestCase):
    def setUp(self):
        self.user_data = {"username": "testuser", "password": "testpassword"}
        self.user = User.objects.create_user(
            username="testuser", password="testpassword", email="test@gmail.com")
        self.token = Token.objects.create(user=self.user)
        self.profile = Profile
        self.cls = Class.objects.create(instructor=self.user, profile=Profile.objects.get(
            user=self.user), title="test title", category="test category", content="test content", thumbnail="")

    # 로그인을 안한 상태
    def test_delete_class_not_login(self):
        pk = self.cls.id
        url = '/classes/' + str(pk) + '/'
        print(url)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 401)

    # 로그인을 한 상태
    def test_delete_class_login(self):
        pk = self.cls.id
        url = '/classes/' + str(pk) + '/'
        response = self.client.delete(
            url, HTTP_AUTHORIZATION="Token " + str(self.token))
        self.assertEqual(response.status_code, 204)
