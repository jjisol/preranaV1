# Generated by Django 3.0.2 on 2020-03-19 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OnedayClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('F', '여'), ('M', '남')], default='F', max_length=1, verbose_name='강사 성별')),
                ('name', models.CharField(max_length=20, verbose_name='클래스명')),
                ('type', models.CharField(choices=[('요가', '요가'), ('필라테스', '필라테스')], default='요가', max_length=4, verbose_name='클래스 종류')),
                ('theme', models.CharField(choices=[('1', '일반'), ('2', '임산부'), ('3', '키즈')], default='1', max_length=1, verbose_name='수업 테마')),
                ('image', models.ImageField(upload_to='class/img/', verbose_name='사진')),
                ('date', models.DateTimeField(verbose_name='날짜')),
                ('day', models.CharField(choices=[('월', '월'), ('화', '화'), ('수', '수'), ('목', '목'), ('금', '금'), ('토', '토'), ('일', '일')], default='월', max_length=1, verbose_name='요일')),
                ('place', models.CharField(max_length=50, verbose_name='장소')),
                ('price', models.PositiveIntegerField(help_text='단위: 원', verbose_name='비용')),
                ('sns', models.CharField(help_text='SNS 아이디를 입력해주세요', max_length=100, verbose_name='SNS 아이디')),
                ('description', models.TextField(verbose_name='간단한 설명')),
            ],
        ),
    ]
