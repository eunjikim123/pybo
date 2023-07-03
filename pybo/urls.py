from django.urls import path
from . import views

app_name = 'pybo'

urlpatterns = [
    # pybo로 시작하는 페이지를 요청하면 이제 pybo/urls.py 파일의 매핑정보를 읽어서 처리
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
     path('question/create/', views.question_create, name='question_create'),
]