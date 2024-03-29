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


# 기존 강의처럼 setUp 메소드로 유저를 생성한 후, 생성한 유저의 데이터로 로그인을 진행하여 상태코드가 200인지 확인하려고 하였으나
# Token matching query does not exist 라는 에러가 발생했다
# 그래서 상태코드를 비교하는 것이 아닌, 생성한 유저의 토큰 값을 가져온 후, 그것을 로그인 진행한 뒤 받은 토큰 값과 비교해서 테스트를 진행한다
class LoginUserTest(APITestCase):
    def setUp(self):
        self.data = {"username": "testuser", "password": "testpassword"}
        self.user = User.objects.create_user(
            username="testuser", password="testpassword", email="test@gmail.com")
        self.token = Token.objects.get_or_create(user=self.user)

    def test_login(self):
        url = reverse('login_view')
        response = self.client.post(url, self.data)
        self.assertEqual(response.status_code, 200)


class LogoutUserTest(APITestCase):
    def test_logout(self):
        url = reverse('logout_view')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 202)
