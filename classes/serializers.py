from rest_framework import serializers
from users.serializers import ProfileSerializer
from .models import Class


class ClassSerializer(serializers.ModelSerializer):
    # profile 필드를 따로 정의하는 이유는, 이를 작성하지 않을 경우에는
    # 기본적으로 profile 필드에 profile의 pk 값만 나타나기 때문이다.
    profile = ProfileSerializer(read_only=True)  # nested serializer

    class Meta:
        model = Class
        fields = ("profile", "title", "category", "content",
                  "thumbnail", "student", "recommend", "register_dttm")


# 수업을 등록할 때 user가 입력해주는 정보는 제목, 카테고리, 내용, 썸네일 정도 뿐이다.
# 나머지 데이터 (강사, 등록날짜 등)들은 코드가 알아서 채워주거나 처음에는 빈칸(추천, 수강여부)으로 두게 되는 경우도 있다.
# 그래서 해당 수업에 대한 내용을 전달해야 하는 serializer와는 다를 필요가 있기 때문에 serializer를 구분하여 작성한다.
class ClassCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ("title", "category", "content", "thumbnail")
