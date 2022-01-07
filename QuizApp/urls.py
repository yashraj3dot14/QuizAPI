from django.urls import path
from . import views

urlpatterns = [
    path('', views.Quiz.as_view(), name= 'quiz'),
    path('q/<str:topic>',views.QuestionClassView.as_view(), name= 'question_list'),
    path('r/<str:topic>', views.RandomQuestionClassView.as_view(), name= 'random_question'),
]