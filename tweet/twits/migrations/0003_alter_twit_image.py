# Generated by Django 3.2.7 on 2022-03-19 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twits', '0002_alter_twit_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='twit',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='users/%Y/%m/%d/'),
        ),
    ]
