# Generated by Django 3.2 on 2021-05-03 07:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='QnaCategory',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category_name', models.CharField(blank=True, max_length=255, null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'QnA_category',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('question', models.CharField(blank=True, max_length=100, null=True)),
                ('question_type', models.CharField(blank=True, max_length=100, null=True)),
                ('is_mandatory', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('category_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question_set_category', to='QnA.qnacategory')),
                ('ques_sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'question',
            },
        ),
        migrations.CreateModel(
            name='Choices',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('choice_1', models.CharField(blank=True, max_length=100, null=True)),
                ('choice_2', models.CharField(blank=True, max_length=100, null=True)),
                ('choice_3', models.CharField(blank=True, max_length=100, null=True)),
                ('choice_4', models.CharField(blank=True, max_length=100, null=True)),
                ('question', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='choice_set_question', to='QnA.question')),
            ],
            options={
                'verbose_name_plural': 'choice',
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('ques_answer', models.CharField(blank=True, max_length=100, null=True)),
                ('is_match', models.BooleanField(default=False)),
                ('ques_sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer_set_user', to=settings.AUTH_USER_MODEL)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer_set_question', to='QnA.question')),
                ('receiver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='receiver_set_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'answer',
            },
        ),
    ]
