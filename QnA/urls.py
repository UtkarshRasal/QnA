from rest_framework.routers import DefaultRouter
from QnA import views
from django.urls import include, path

router = DefaultRouter()
router.register(r'questions', views.QuestionView, basename='question')
router.register(r'category', views.CategoryTypeView, basename='category')

urlpatterns = [
    path('', include(router.urls)),
    path('selectedQnA/', views.SelectedQnAView.as_view())
]