from django.db import models
from base.models import BaseModel
from accounts.models import User

class QnaCategory(BaseModel):
    category_name = models.CharField(max_length=255, blank=False)

    class Meta:
        verbose_name_plural = 'QnA_category'
        ordering = ['-created_at']

    def __str__(self):
        return self.category_name

class Question(BaseModel):

    ques_sender = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.CharField(max_length=255, null=True, blank=True)
    correct_answer = models.CharField(max_length=100, null=True, blank=True)

    category_type = models.ManyToManyField(QnaCategory)
    question_type = models.CharField(max_length=100, choices=[('Objective', 'Objective'),('Subjective', 'Subjective')], null=True, blank=True)
    is_mandatory = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'question'

    def __str__(self):
        return self.question

class Choices(BaseModel):
    
    question = models.OneToOneField(Question, on_delete=models.CASCADE, related_name="choice_set_question")
    choice_1 = models.CharField(max_length=100, null=True, blank=True)
    choice_2 = models.CharField(max_length=100, null=True, blank=True)
    choice_3 = models.CharField(max_length=100, null=True, blank=True)
    choice_4 = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'choice'
        ordering = ['-created_at']
        
    def __str__(self):
        return str(self.question.question)

class Answer(BaseModel):
    
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="answer_set_question")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE)

    answer = models.CharField(max_length=100, null=True, blank=True)
    is_correct = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'answer'
        ordering = ['-created_at']
    
    def __str__(self):
        return self.answer

class SelectedQnA(BaseModel):
    ques_sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ques_sender')
    question = models.ManyToManyField(Question, blank=True)
    answer = models.ManyToManyField(Answer, blank=True)
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'SelectedQnA'
        ordering = ['-created_at']
    
    