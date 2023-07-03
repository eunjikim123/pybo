from django.contrib import admin

# Register your models here.
from .models import Question,Answer

#제목(subject)으로 질문 데이터를 검색
class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)