# Generated by Django 3.2.7 on 2022-03-23 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twits', '0006_alter_twit_users_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_datetime',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
