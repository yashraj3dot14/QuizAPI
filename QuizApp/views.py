from django.shortcuts import render
from rest_framework import generics
from .models import Category,Quizzes,Question,Answer
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import QuizSerializer,QuestionSerializer, RandomQuestionSerializer
# Create your views here.

class Quiz(generics.ListAPIView):
    queryset = Quizzes.objects.all()
    serializer_class = QuizSerializer

class QuestionClassView(APIView):
    def get(self, request, format= None, **kwargs):
        question = Question.objects.filter(quiz__title= kwargs['topic']) #it will got to backward, from model-Question to model-Quiz and fetch quiz title
        serializer = QuestionSerializer(question, many= True)
        return Response(serializer.data)

class RandomQuestionClassView(APIView):
    def get(self, request, format= None, **kwargs):
        randQuestion = Question.objects.filter(quiz__title = kwargs['topic']).order_by('?')[:1]
        serializer = RandomQuestionSerializer(randQuestion, many = True)
        return Response(serializer.data)