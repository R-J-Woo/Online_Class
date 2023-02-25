from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator  # 중복 방지를 위해 사용
from django.contrib.auth import authenticate
from .models import Profile


# 회원가입 시리얼라이저
class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        # 이메일에 대한 중복 검증
        validators=[UniqueValidator(queryset=User.objects.all())],
    )
    password = serializers.CharField(
        write_only=True,  # write_only: 클라이언트 -> 서버의 역직렬화만 가능, 서버 -> 클라이언트의 직렬화는 불가능
        required=True,
        validators=[validate_password],  # 비밀번호에 대한 검증
    )
    password2 = serializers.CharField(
        write_only=True, required=True
    )

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email')

    # 추가적으로 비밀번호 일치 여부 확인
    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError(
                {"password": "비밀번호가 같지 않습니다."}  # 비밀번호와 확인이 같지 않으면 에러 표시
            )

        return data

    def create(self, validated_data):
        # create 메소드를 오버라이딩, 유저를 생성하고 토큰을 생성하도록 함
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
        )

        user.set_password(validated_data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return user


# 로그인 시리얼라이저
class LoginSerailizer(serializers.Serializer):
    username = serializers.CharField(required=True)  # username을 회원 아이디로 사용
    password = serializers.CharField(required=True, write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user:  # 사용자가 존재하면 토큰 발급
            token = Token.objects.get(user=user)
            return token
        raise serializers.ValidationError(
            {"error": "입력하신 정보에 해당하는 사용자가 존재하지 않습니다."}
        )


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("nickname", "image")
