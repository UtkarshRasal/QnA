# Generated by Django 3.1.7 on 2021-04-24 20:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['created_at'], 'verbose_name_plural': 'User'},
        ),
    ]
