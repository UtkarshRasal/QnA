from django.contrib import admin
from .models import QnaCategory, Question, Choices, Answer, SelectedQnA

admin.site.register(QnaCategory)
admin.site.register(Question)
admin.site.register(Choices)
admin.site.register(Answer)
admin.site.register(SelectedQnA)

