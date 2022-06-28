from django.db import models

# Create your models here.




class Quiz(models.Model):
    title = models.CharField(max_length=20)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name        

class Question(models.Model):
    title = models.CharField(max_length=20)
    DIFFICULTY = (
       ('H', 'High'),
       ('M', 'Medium'),
       ('L', 'Low'),
    )
    difficulty = models.CharField(max_length=5, choices=DIFFICULTY, default='L')
    date_created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title 


class Answer(models.Model):
    answer_text = models.CharField(max_length=30)
    is_right = models.CharField(max_length=30)
    updated = models.DateTimeField(auto_now=True)   