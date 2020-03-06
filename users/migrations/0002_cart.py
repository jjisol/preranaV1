# Generated by Django 3.0.2 on 2020-02-26 07:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
       
        ('onedayclass', '0004_auto_20200226_1600'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('center', models.ManyToManyField(related_name='cart_center', to='center.Center', verbose_name='센터')),
                ('event', models.ManyToManyField(related_name='cart_event', to='center.Center', verbose_name='이벤트')),
                ('onedayclass', models.ManyToManyField(related_name='cart_onedayclass', to='onedayclass.OnedayClass', verbose_name='원데이클래스')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='사용자')),
            ],
        ),
    ]
