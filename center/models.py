from django.db import models
from django.utils import timezone
from multiselectfield import MultiSelectField

class Center(models.Model):
    TYPE_CHOICES = [('요가', '요가'), ('필라테스', '필라테스'),]

    CENTER_CHOICES = [('1', '여성전용'), ('2', '여남공용'), ('3', '남성전용')]

    name = models.CharField(max_length=20, verbose_name='센터명')
    type = MultiSelectField(
        choices=TYPE_CHOICES,
        verbose_name='센터 종류')
    detail = models.CharField(max_length=1,
        choices=CENTER_CHOICES,
        default='1',
        verbose_name='전용시설')
    price = models.TextField(verbose_name='이용가격')
    info = models.TextField(verbose_name='이용정보')
    event = models.ImageField(null=True, verbose_name='이벤트', upload_to='center/event/')
    schedule = models.ImageField(null=True, help_text="스케줄표를 이미지로 업로드해주세요",
        verbose_name='스케줄표', upload_to='center/schedule/')
    phone = models.CharField(max_length=20, verbose_name='센터 전화번호')
    address = models.CharField(max_length=200, verbose_name='센터 주소')
    site = models.URLField(max_length=250, verbose_name='센터 사이트 주소')

    def __str__(self):
        return self.name

class CenterImage(models.Model):
    center = models.ForeignKey(Center, on_delete=models.CASCADE,
                    related_name='center_image', verbose_name='센터명')
    image1 = models.ImageField(null=True, verbose_name='센터 사진1', upload_to='center/img/')
    image2 = models.ImageField(null=True, verbose_name='센터 사진2', upload_to='center/img/')
    image3 = models.ImageField(null=True, verbose_name='센터 사진3', upload_to='center/img/')

    def __str__(self):
        return self.center.name

class CenterReview(models.Model):
    center = models.ForeignKey(Center, on_delete=models.CASCADE,
                    related_name='center_review', verbose_name='센터명')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text
