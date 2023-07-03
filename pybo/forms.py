from django import forms
from pybo.models import Question,Answer



# QuestionFrom 은 Question 모델과 연결된 폼이고 속성으로 Question 모델의 subject 와 content 를 사용함
class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question # 사용할 모델
        fields = ['subject','content'] # QuestionForm 에서 사용할 Question 모델의 속성
        
        labels = {
            'subject': '제목',
            'content': '내용',
        }  


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '답변내용',
        }

