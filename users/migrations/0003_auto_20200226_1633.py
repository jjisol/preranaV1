# Generated by Django 3.0.2 on 2020-02-26 07:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_cart'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='center',
            new_name='centers',
        ),
        migrations.RenameField(
            model_name='cart',
            old_name='event',
            new_name='events',
        ),
        migrations.RenameField(
            model_name='cart',
            old_name='onedayclass',
            new_name='onedayclasses',
        ),
    ]
