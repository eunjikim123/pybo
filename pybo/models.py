from django.db import models

# Create your models here.
class Question(models.Model):
    
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    
    
    # def__str__ 이케 해주면 객체 안의 값이 리턴된다
    def __str__(self):
        return self.subject

        

class Answer(models.Model):
    
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    
    