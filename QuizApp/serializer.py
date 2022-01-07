from rest_framework import serializers
from .models import Quizzes,Answer,Question

class QuizSerializer(serializers.ModelSerializer):

    class Meta:
        model = Quizzes
        fields = [
            'title',
        ]

class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = [
            'answer_text', 'is_right',
        ]

class QuestionSerializer(serializers.ModelSerializer):

    quiz = QuizSerializer(read_only= True)
    answer = AnswerSerializer(many= True, read_only= True)
    class Meta:
        model = Question
        fields = [
            'quiz','title', 'difficulty', 'is_active','answer',
        ]


class RandomQuestionSerializer(serializers.ModelSerializer):

    answer = AnswerSerializer(many= True, read_only= True)
    class Meta:
        model = Question
        fields = [
            'title', 'answer',
        ]