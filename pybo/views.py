# render 함수는 파이썬 데이터를 템플릿에 적용하여 html 로 반환하는 함수
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseNotAllowed
from django.utils import timezone

# Create your views here.
#from django.http import HttpResponse

from .models import Question, Answer
from .forms import QuestionForm,AnswerForm



def index(request):
    # httpresponse 는 요청에 대한 응답을 할때 사용
    #return HttpResponse("안녕하세요 pybo에 오신것을 환영합니다.")
    
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list':question_list}
    
    # 파이썬 데이터를 html 로 변경한뒤 r
    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    
    question = get_object_or_404(Question, pk=question_id)
    #question = Question.objects.get(id=question_id)
    context = {'question': question}
    
    return render(request, 'pybo/question_detail.html', context)

def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    #question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    answer = Answer(question=question, content = request.POST.get('content'), create_date = timezone.now())
    answer.save()
    return redirect('pybo:detail', question_id=question.id)


def question_create(request):
    
    # url.py를 통하면 무조건 request.method 는 get 이 되어 넘어온다
    
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False) # 임시 저장하여 question 객체를 리턴받는다.
            question.create_date = timezone.now() # 실제 저장을 위해 작성일시를 설정한다.
            question.save() # 데이터를 실제로 저장한다.
            return redirect('pybo:index')
    else:
        form = QuestionForm()
    
    context = {'form':form}    
    
    
    return render(request, 'pybo/question_form.html', {'form': form})


     
def answer_create(request, question_id):
    
    # question_detail html 부분의 form 이랑 연결된 부분
    """
    pybo 답변등록
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        return HttpResponseNotAllowed('Only POST is possible.')
    context = {'question': question, 'form': form}
    return render(request, 'pybo/question_detail.html', context)