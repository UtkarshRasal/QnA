from django.shortcuts import render
from .serializers import QuestionsCreateSerializer
from base.viewsets import BaseViewSet
from .models import Question

class QuestionAnswerView(BaseViewSet):
    model_class = Question
    serializer_class = QuestionsCreateSerializer
    instance_name = 'Question'

    def get_serializer_class(self):
        return self.serializer_class