# Generated by Django 3.1 on 2020-10-27 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0019_comment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
