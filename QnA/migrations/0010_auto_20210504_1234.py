# Generated by Django 3.1.7 on 2021-05-04 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QnA', '0009_remove_question_receiver'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='category_type',
            field=models.ManyToManyField(to='QnA.QnaCategory'),
        ),
    ]
