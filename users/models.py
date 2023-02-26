from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    nickname = models.CharField(max_length=128)
    image = models.ImageField(upload_to='profile/',
                              default='profile/default.png')


# User모델이 post_save 이벤트를 발생시켰을 때, 해당 user와 연결되는 profile도 동시에 생성해준다
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
