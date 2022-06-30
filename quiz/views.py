from django.shortcuts import render
from .models import Category, Quiz, Question, Answer
from .serializers import CategorySerializer, QuizSerializer, QuestionSerializer, AnswerSerializer
from rest_framework.decorators import action
from rest_framework import  viewsets
from rest_framework.response import Response
from .permission import IsAuthOrNot
from rest_framework.generics import ListAPIView



class CategoryView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class QuizView(ListAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer 
    permission_classes=(IsAuthOrNot,)  

    def get_queryset(self):
       category = self.kwargs['category']
       return Quiz.objects.filter(category__name__iexact=category)
  


class QuestionSerializer(ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes=(IsAuthOrNot,)   

    def get_queryset(self):
       title = self.kwargs['title']
       return Question.objects.filter(quiz__title__iexact=title)

