from django.db import models
from django.utils import timezone

# Create your models here.
class OnedayClass(models.Model):
    TYPE_CHOICES = [('Y', '요가'), ('P', '필라테스'),]

    THEME_CHOICES = [('1', '일반'), ('2', '임산부'), ('3', '키즈'),]

    GENDER_CHOICES = [('F', '여'), ('M', '남'),]

    DAY_CHOICES = [('월', '월'), ('화', '화'), ('수', '수'),
    ('목', '목'), ('금', '금'), ('토', '토'), ('일', '일'),]

    gender = models.CharField(max_length=1,
        choices=GENDER_CHOICES,
        default='F',
        verbose_name='강사 성별')
    name = models.CharField(max_length=20, verbose_name='클래스명')
    type = models.CharField(max_length=1,
        choices=TYPE_CHOICES,
        default='Y',
        verbose_name='클래스 종류')
    theme = models.CharField(max_length=1,
        choices=THEME_CHOICES,
        default='1',
        verbose_name='수업 테마')
    image = models.ImageField(verbose_name='사진', upload_to='class/img/')
    date = models.DateTimeField(verbose_name='날짜')
    day = models.CharField(max_length=1,
        choices=DAY_CHOICES,
        default='월',
        verbose_name='요일')
    place = models.CharField(max_length=50, verbose_name='장소')
    price = models.PositiveIntegerField(verbose_name='비용', help_text='단위: 원')
    sns = models.CharField(max_length=100,
        help_text="SNS 아이디를 입력해주세요",
        verbose_name='SNS 아이디')
    description = models.TextField(verbose_name='간단한 설명')

    def __str__(self):
        return self.name
