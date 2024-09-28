# Generated by Django 3.2.7 on 2022-03-22 05:40

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('twits', '0003_alter_twit_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='twit',
            name='user_like',
            field=models.ManyToManyField(blank=True, related_name='twits_like', to=settings.AUTH_USER_MODEL),
        ),
    ]
