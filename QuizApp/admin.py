from django.contrib import admin
from . import models
# Register your models here.

#below code will add new category option in admin pannel
@admin.register(models.Category)
class CatAdmin(admin.ModelAdmin):
    list_display = [
        'name'
    ]

@admin.register(models.Quizzes)
class QuizAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
    ]

class AnswerInlineModel(admin.TabularInline):

    model = models.Answer
    fields = [
        'answer_text',
        'is_right',
    ]

@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
    fields = [
        'title', #fields which we have defined in models.py
        'quiz',
        'difficulty',
    ]

    list_display = [
        'title',
        'quiz',
        'date_updated',
    ]

    inlines = [
        AnswerInlineModel,
    ]

@admin.register(models.Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = [
        'question',
        'answer_text',
        'is_right',
    ]