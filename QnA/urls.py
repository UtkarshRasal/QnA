from rest_framework.routers import DefaultRouter
from QnA import views
from django.urls import include, path

router = DefaultRouter()
router.register(r'questions', views.QuestionAnswerView, basename='questions')

urlpatterns = [
    path('', include(router.urls))
]