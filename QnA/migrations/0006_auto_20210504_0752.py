# Generated by Django 3.1.7 on 2021-05-04 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QnA', '0005_auto_20210504_0751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_type',
            field=models.CharField(blank=True, choices=[('Objective', 'Subjective'), ('Subjective', 'Objective')], max_length=100, null=True),
        ),
    ]
