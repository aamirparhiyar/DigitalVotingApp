# Generated by Django 2.1.7 on 2019-03-30 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0008_auto_20190329_1148'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Constituency',
        ),
        migrations.AlterField(
            model_name='voter',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='profile_images'),
        ),
    ]
