from django.contrib import admin
from .models import Category, Quiz, Question, Answer

# import nested_admin
# from nested_admin import NestedModelAdmin, NestedStackedInline


# class Quizline(nested_admin.NestedStackedInline):
#     model = Quiz
#     sortable_field_name = "category"
 

# class Questionline(nested_admin.NestedStackedInline):
#     model = Question
#     sortable_field_name = "title"
#     inlines = [Quizline]

# class Answerline(nested_admin.NestedStackedInline):
#     model = Answer
#     sortable_field_name = "question"
#     inlines = [Questionline]


# class CategoryAdmin(nested_admin.NestedModelAdmin):
#     inlines = [Answerline]




# class Categoryline(nested_admin.NestedStackedInline):
#     model = Category
#     sortable_field_name = "category"

# class Quizline(nested_admin.NestedStackedInline):
#     model = Quiz
#     sortable_field_name = "title"
#     inlines = [Categoryline]

# class Questionline(nested_admin.NestedStackedInline):
#     model = Question
#     sortable_field_name = "title"
#     inlines = [Quizline]








# admin.site.register(CategoryAdmin)
admin.site.register(Category)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Answer)

