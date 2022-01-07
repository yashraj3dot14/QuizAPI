from django.shortcuts import render
from rest_framework import generics
from .models import Category,Quizzes,Question,Answer
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import QuizSerializer
# Create your views here.

class Quiz(generics.ListAPIView):
    queryset = Quizzes.objects.all()
    serializer_class = QuizSerializer()