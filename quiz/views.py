from django.shortcuts import render
from .models import Category, Quiz, Question, Answer
from .serializers import CategorySerializer, QuizSerializer, QuestionSerializer, AnswerSerializer
from rest_framework.decorators import action
from rest_framework import  viewsets
from rest_framework.response import Response
from .permissions import IsAuthOrNot
from rest_framework.generics import ListAPIView

# class CategoryView(viewsets.ModelViewSet):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer

class CategoryView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class QuizView(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer   

    def get_queryset(self):
       category = self.kwargs['category']
       return Category.objects.filter(quiz__category=category)
