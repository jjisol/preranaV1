# Generated by Django 3.0.2 on 2020-02-26 07:00

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('center', '0005_auto_20200210_0152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='center',
            name='type',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('요가', '요가'), ('필라테스', '필라테스')], max_length=7, verbose_name='센터 종류'),
        ),
    ]
