from django.shortcuts import render
from .models import Category, Quiz, Question, Answer
from .serializers import CategorySerializer, QuizSerializer, QuestionSerializer, AnswerSerializer
from rest_framework.decorators import action
from rest_framework import  viewsets
from rest_framework.response import Response


class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @action(methods=["GET"], detail=False)
    def quiz_count(self, request):
        quiz_count = Quiz.objects.all().count()

        count = {
            'quiz_count': quiz_count
        }

        return Response(count)



