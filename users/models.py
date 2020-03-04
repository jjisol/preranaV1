from django.contrib.auth.models import AbstractUser
from django.db import models
from center.models import Center
from onedayclass.models import OnedayClass

class CustomUser(AbstractUser):

    def __str__(self):
        return self.username

class Cart(models.Model):
    user = models.ForeignKey(CustomUser, null=True, blank=True,
     on_delete=models.CASCADE,
     verbose_name='사용자')
    centers = models.ManyToManyField(Center, related_name='cart_center', verbose_name='센터')
    events = models.ManyToManyField(Center, related_name='cart_event', verbose_name='이벤트')
    onedayclasses = models.ManyToManyField(OnedayClass, related_name='cart_onedayclass', verbose_name='원데이클래스')

    def __str__(self):
        return self.user.username
