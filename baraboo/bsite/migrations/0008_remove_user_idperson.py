# Generated by Django 2.1.1 on 2018-09-13 02:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bsite', '0007_user_idperson'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='idPerson',
        ),
    ]