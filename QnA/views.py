from base.response import return_response
from base.viewsets import CategoryViewSet, QuestionViewSet
from django.shortcuts import render
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from QnA import mixins

from .models import QnaCategory, Question, SelectedQnA
from .serializers import (CategoryTypeSerializer, ChoiceSerializer,
                          QuestionsCreateSerializer, AnswerSerializer,
                          QuestionShowSerializer, SelectedQnASerializer)


class CategoryTypeView(CategoryViewSet):
    model_class = QnaCategory
    serializer_class = CategoryTypeSerializer
    instance_name = 'Category'

    def get_serializer_class(self):
        return self.serializer_class

class QuestionView(QuestionViewSet, mixins.ChoiceMixin, mixins.AnswerMixin):
    model_class = Question
    serializer_class = QuestionsCreateSerializer
    instance_name = 'Question'

    ACTION_SERIALIZER = {
        'list': QuestionShowSerializer,
        'choices':ChoiceSerializer,
        'answer':AnswerSerializer,
    }

    def get_serializer_class(self):
        return self.ACTION_SERIALIZER.get(self.action, self.serializer_class)

class SelectedQnAView(APIView):
    serializer_class = SelectedQnASerializer
    model_class = SelectedQnA

    def get(self, request):

        queryset = self.model_class.objects.all()
        return Response(self.serializer_class(queryset, many=True).data)