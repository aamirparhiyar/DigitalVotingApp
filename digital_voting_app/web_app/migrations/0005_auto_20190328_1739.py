# Generated by Django 2.1.7 on 2019-03-28 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0004_auto_20190328_0009'),
    ]

    operations = [
        migrations.AddField(
            model_name='voter',
            name='image',
            field=models.ImageField(blank=True, upload_to='profile_image'),
        ),
        migrations.AlterField(
            model_name='voter',
            name='contact_num',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='voter',
            name='email_id',
            field=models.CharField(max_length=345),
        ),
        migrations.AlterField(
            model_name='voter',
            name='photograph_image_link',
            field=models.URLField(default=''),
        ),
        migrations.AlterField(
            model_name='voter',
            name='signature_image_link',
            field=models.URLField(default=''),
        ),
    ]
