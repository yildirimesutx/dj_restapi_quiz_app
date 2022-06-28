from django.contrib import admin
from .models import Category, Quiz, Question, Answer

# import nested_admin



# class Quizline(nested_admin.NestedStackedInline):
#     model = Quiz
#     sortable_field_name = "position"
 

# class Questionline(nested_admin.NestedStackedInline):
#     model = Question
#     sortable_field_name = "position"
#     inlines = [Quizline]

# class Answerline(nested_admin.NestedStackedInline):
#     model = Answer
#     sortable_field_name = "position"
#     inlines = [Questionline]


# class CategoryAdmin(nested_admin.NestedModelAdmin):
#     inlines = [Answerline]



admin.site.register(Category)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Answer)

