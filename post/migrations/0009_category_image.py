# Generated by Django 3.1 on 2020-09-07 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0008_post_alt'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(default=True, upload_to='images/'),
        ),
    ]
