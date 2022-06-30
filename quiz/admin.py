from django.contrib import admin
import nested_admin
from .models import Category, Quiz, Question, Answer




class AnswerInline(nested_admin.NestedStackedInline):
    model = Answer



class QuestionInline(nested_admin.NestedStackedInline):
    model = Question
   
    inlines = [AnswerInline]

class QuizInline(nested_admin.NestedStackedInline):
    model = Quiz
   
    inlines= [QuestionInline]

class CategoryAdmin(nested_admin.NestedModelAdmin):
    inlines = [QuizInline]

admin.site.register(Category,CategoryAdmin)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Answer)

