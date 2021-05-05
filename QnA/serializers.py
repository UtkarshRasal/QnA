from rest_framework.serializers import ModelSerializer
from .models import QnaCategory, Question, Answer, SelectedQnA, Choices

class CategoryTypeSerializer(ModelSerializer):

    class Meta:
        model = QnaCategory
        fields = ['category_name']

class QuestionsCreateSerializer(ModelSerializer):
    category_type = CategoryTypeSerializer(read_only=True, many=True)

    class Meta:
        model = Question
        fields = ['id','ques_sender', 'question', 'question_type', 'category_type', 'created_at', 'updated_at']
    
    ''' category create and update'''
    def create(self, validated_data):
        import pdb;pdb.set_trace()
        _category = validated_data.get("category_type", [])
        category_list = []
        for category in _category:
            _category, _ = QnaCategory.objects.get_or_create(**category)
            category_list.append(_category.pk)

        _question = Question.objects.create(**validated_data)

        _question.category_type.set(category_list)

        return _question

    def update(self, instance, validated_data):
        _category = validated_data.pop("category_type", [])
        category_list = []
        for category in _category:
            _category, _ = QnaCategory.objects.get_or_create(**category)
            category_list.append(_category.pk)
        instance.category_type.clear()
        instance.category_type.set(tag_list)

        return super(BlogsSerializer,
                     self).update(instance, validated_data)
    