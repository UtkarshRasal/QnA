# Generated by Django 3.1.7 on 2021-05-04 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QnA', '0003_auto_20210504_0737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_type',
            field=models.CharField(blank=True, choices=[('Objective', 'Subjective')], max_length=100, null=True),
        ),
    ]
