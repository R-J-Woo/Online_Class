from django.urls import reverse
from rest_framework.test import APITestCase, force_authenticate
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


# Create your tests here.
# 회원가입 테스트


class UserRegisterTest(APITestCase):
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

    # 로그인 테스트 할 때 회원가입과 마찬가지로 user_data를 설정했는데 안되는 이유는
    # 모든 테스트 메소드를 실행할 때마다 장고에서는 테스트 DB를 초기화하기 때문이다
    # 그래서 회원가입에 입력했던 user_data를 로그인할 때 그대로 사용하더라도 에러가 발생한다 -> SetUp 메소드 필요

    # def test_login(self):
    #     url = reverse('login_view')
    #     user_data = {
    #         "username": "testusername",
    #         "password": "testpassword",
    #     }
    #     response = self.client.post(url, user_data)
    #     # 로그인 진행 후의 상태 코드가 200인지 확인
    #     self.assertEqual(response.status_code, 200)


class LoginUserTest(APITestCase):
    def setUp(self):
        self.data = {"username": "testuser", "password": "testpassword"}
        self.user = User.objects.create_user(
            username="testuser", password="testpassword", email="test@gmail.com")
        self.token = Token.objects.create(user=self.user)

    def test_login(self):
        url = reverse('login_view')
        response = self.client.post(url, self.data)
        self.assertEqual(response.data["token"], self.token.key)
