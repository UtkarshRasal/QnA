# Generated by Django 3.1.7 on 2021-05-05 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('QnA', '0002_auto_20210505_1557'),
    ]

    operations = [
        migrations.RenameField(
            model_name='selectedqna',
            old_name='reciever',
            new_name='receiver',
        ),
    ]