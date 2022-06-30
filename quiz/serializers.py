from rest_framework import serializers
from .models import Category, Quiz, Question, Answer




class CategorySerializer(serializers.ModelSerializer):
    
    quiz_count= serializers.SerializerMethodField()
  
    class Meta :
        model = Category
        # fields = '__all__'
        fields = [
           'id',
           'name',
           'quiz_count' 
        ]
    def get_quiz_count(self, obj):
       return Quiz.objects.filter(category_id=obj.id).count() 
       

class QuizSerializer(serializers.ModelSerializer):

    question_count = serializers.SerializerMethodField()
    class Meta :
        model = Quiz
        # fields = '__all__'
        fields = [
            "id",
            "category",
            "title",
            "question_count"
        ]
    def get_question_count(self, obj):
       return Question.objects.filter(quiz_id=obj.id).count() 

class QuestionSerializer(serializers.ModelSerializer):
    class Meta :
        model = Question
        fields = '__all__'


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = fields = '__all__'

