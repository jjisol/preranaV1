from django.db import models
from multiselectfield import MultiSelectField
from center.models import Center
from django.utils import timezone

# Create your models here.
class Certificate(models.Model):
    name = models.CharField(max_length=20, verbose_name='자격증')

    def __str__(self):
        return self.name

class Yoga(models.Model):
    name = models.CharField(max_length=20, verbose_name='요가종류')

    def __str__(self):
        return self.name

class Instrument(models.Model):
    name = models.CharField(max_length=20, verbose_name='필라테스기구')

    def __str__(self):
        return self.name

class VisitingArea(models.Model):
    gu = models.CharField(max_length=10, verbose_name='방문가능지역')

    def __str__(self):
        return self.gu

class Instructor(models.Model):
    GENDER_CHOICES = (
       ('M', 'Male'),
       ('F', 'Female'),
    )

    name = models.CharField(max_length=10, verbose_name='이름')
    phone = models.CharField(max_length=11, verbose_name='전화번호', help_text='-없이 입력해주세요.')
    gender = models.CharField(max_length=1,
        choices=GENDER_CHOICES,
        default='F',
        verbose_name='성별')
    greeting = models.CharField(max_length=100,
        null=True, verbose_name='간단한 인사말')
    image = models.ImageField(blank=False, verbose_name='사진', upload_to='instructor/img/')
    certificate = models.ManyToManyField(Certificate, verbose_name='보유자격증')
    schedule = models.ImageField(null=True, help_text="개인스케줄표를 이미지로 업로드해주세요.",
        verbose_name='개인스케줄', upload_to='instructor/schedule/')
    sns_url = models.URLField(max_length=250,
        help_text="SNS주소를 입력해주세요",
        verbose_name='SNS주소')
    center = models.ManyToManyField(Center, blank=True, verbose_name='센터',
        help_text="소속되어있거나 관계되어있는 센터들을 선택해주세요.")

    def __str__(self):
        return self.name


class YogaInstructor(models.Model):
    CAREER_CHOICES = (
        ('A', '6개월 미만'),
        ('B', '6개월 이상 1년 미만'),
        ('C', '1년 이상 3년 미만'),
        ('D', '3년 이상'),
    )

    instructor = models.ForeignKey(Instructor,
        on_delete=models.CASCADE,
        verbose_name='이름',
        related_name='yoga_instructor',
        help_text='요가강사의 이름을 선택해주세요.')
    career = models.CharField(max_length=1,
        choices=CAREER_CHOICES,
        default='A',
        verbose_name='경력')
    price = models.TextField(verbose_name='가격')
    style = models.ManyToManyField(Yoga, blank=True, verbose_name='가능한 요가 종류')

    def __str__(self):
        return self.instructor.name

class PilatesInstructor(models.Model):
    CAREER_CHOICES = (
        ('A', '6개월 미만'),
        ('B', '6개월 이상 1년 미만'),
        ('C', '1년 이상 3년 미만'),
        ('D', '3년 이상'),
    )

    instructor = models.ForeignKey(Instructor,
        on_delete=models.CASCADE,
        verbose_name='이름',
        related_name='pilates_instructor',
        help_text='필라테스강사의 이름을 선택해주세요.')
    career = models.CharField(max_length=1,
        choices=CAREER_CHOICES,
        default='A',
        verbose_name='경력')
    price = models.TextField(verbose_name='가격')

    def __str__(self):
        return self.instructor.name

class VisitingInstructor(models.Model):
    CAREER_CHOICES = (
        ('A', '6개월 미만'),
        ('B', '6개월 이상 1년 미만'),
        ('C', '1년 이상 3년 미만'),
        ('D', '3년 이상'),
    )

    instructor = models.ForeignKey(Instructor,
        on_delete=models.CASCADE,
        verbose_name='이름',
        related_name='visiting_instructor',
        help_text='방문수업강사의 이름을 선택해주세요.')
    career = models.CharField(max_length=1,
        choices=CAREER_CHOICES,
        default='A',
        verbose_name='경력')
    price = models.TextField(verbose_name='가격')
    instrument = models.ManyToManyField(Instrument,
        blank=True,
        verbose_name='필라테스 기구')
    visiting_area = models.ManyToManyField(VisitingArea, blank=True,
        verbose_name='방문가능지역',
        help_text='방문수업이 가능한 지역을 선택해주세요.')

    def __str__(self):
        return self.instructor.name
