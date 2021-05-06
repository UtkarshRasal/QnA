from base.response import return_response
from rest_framework.decorators import action
from rest_framework import status, permissions
from .models import Answer 

class ChoiceMixin:
    @action(methods=['POST'], detail=True)
    def choices(self, request, pk, *args, **kwargs):
        assert self.model_class is not None
        try:
            if not self.model_class.objects.filter(id=pk).exists():
                return return_response(False, f"No such {self.instance_name} found", serializer.errors, status.HTTP_400_BAD_REQUEST)
            
            serializer = self.get_serializer(data={**request.data, **{'question':pk}})
            
            serializer.is_valid(raise_exception=True)
            serializer.save()

            
            return return_response(True, f"Choices for {self.instance_name} '{pk}' created successfully", serializer.data, status.HTTP_201_CREATED)
        
        except Exception:
            return return_response(False, f"Choices for the {self.instance_name} '{pk}' already created", serializer.data, status.HTTP_201_CREATED)

class AnswerMixin:
    
    @action(methods=['POST'], detail=True)
    def answer(self, request, pk, *args, **kwargs):
        assert self.model_class is not None
        if not self.model_class.objects.filter(id=pk).exists():
                return return_response(False, f"No such {self.instance_name} found", serializer.errors, status.HTTP_400_BAD_REQUEST)
        
        answer = request.data

        serializer = self.get_serializer(data={**answer, **{'receiver':request.user.pk, 'question':pk}})
        serializer.is_valid(raise_exception=True)
        answer = serializer.save()
        
        question = self.model_class.objects.get(id=pk)
        
        if answer.answer == question.correct_answer:
            answer.is_correct = True
            answer.save()

            serializer = self.get_serializer(answer)

            return return_response(True, "Answer is correct", serializer.data, status.HTTP_202_ACCEPTED)
        
        return return_response(False, "Answer is incorrect", serializer.data, status.HTTP_400_BAD_REQUEST)



            



