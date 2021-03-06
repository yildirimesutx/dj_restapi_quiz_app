from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name 


class Quiz(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.title



class Question(models.Model):
    title = models.CharField(max_length=20)
    quiz =  models.ForeignKey(Quiz, on_delete=models.CASCADE)
    DIFFICULTY = (
       ('High', 'High'),
       ('Medium', 'Medium'),
       ('Low', 'Low'),
    )
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY, default='Low')
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.title 



class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE,related_name='answers')
    answer_text = models.CharField(max_length=30)
    is_right = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True, null=True)  

    def __str__(self):
        return self.answer_text
