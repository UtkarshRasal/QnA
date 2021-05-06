from rest_framework import serializers
from .models import QnaCategory, Question, Answer, SelectedQnA, Choices

class CategoryTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = QnaCategory
        fields = ['id', 'category_name']

class QuestionsCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = ['id','ques_sender', 'question', 'correct_answer', 'question_type', 'category_type', 'created_at', 'updated_at']

class ChoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Choices
        fields = ['id', 'question', 'choice_1', 'choice_2', 'choice_3', 'choice_4']

class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = ['id', 'receiver', 'question', 'answer', 'is_correct', 'created_at']

class QuestionShowSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        exclude = ['correct_answer']
        
class SelectedQnASerializer(serializers.ModelSerializer):

    class Meta:
        model = SelectedQnA
        exclude = ['answer']
