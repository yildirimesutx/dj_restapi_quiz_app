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



class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        # fields = fields = '__all__'
        fields = [
            "answer_text",
            "is_right",
           
        ]




class QuestionSerializer(serializers.ModelSerializer):

    answers = AnswerSerializer(many=True, read_only=True)
    # answer_id = serializers.IntegerField(read_only=True, required=False)
    # answer = serializers.StringRelatedField() 

    class Meta :
        model = Question
        # fields = '__all__'
        fields = [
            "title",
            # "answer_text",
            "answers",
            "difficulty"
        ]




