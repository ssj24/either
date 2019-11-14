from django.shortcuts import render, redirect
from .models import Question, Answer
import random

# Create your views here.
def index(request):
    questions = Question.objects.order_by('pk')
    # random_question = Question.objects.order_by('?').first()
    context = {'questions' : questions,}
    return render(request, 'eithers/index.html', context)


def new(request):
    return render(request, 'eithers/new.html')


def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        issue_a = request.POST.get('issue_a')
        issue_b = request.POST.get('issue_b')
        image_a = request.FILES.get('image_a')
        image_b = request.FILES.get('image_b')

        question = Question(title=title, issue_a=issue_a, issue_b=issue_b, image_a=image_a, image_b=image_b)
        question.save()
        return redirect('/eithers/')
    else:
        return redirect('/eithers/')


def detail(request, question_pk):
    question = Question.objects.get(pk=question_pk)
    # question = Question.objects.prefetch_related('answer_set').get(pk=question_pk) # 얘는 윗줄이랑 동일한 기능인데 렌더되는 페이지에서 프리패치로 불러온 항목을 쓸 때 쿼리를 다시 보내지 않는..모델 최적화 관련
    answers = question.answer_set.order_by('-pk')
    zero, one = 0, 0
    for answer in answers:
        if answer.pick == 0:
            zero += 1
        elif answer.pick == 1:
            one += 1
    if zero > 0 or one > 0:
        l, r = round((zero / (zero+one))*100), round((one / (zero+one))*100)
    else:
        l, r = 0, 0
    context = {'answers' : answers, 'question': question, 'l': l, 'r': r,}
    return render(request, 'eithers/detail.html', context)


def comments_create(request, question_pk):
    if request.method == 'POST':
        question = Question.objects.get(pk=question_pk)
        pick = request.POST.get('pick')
        comment = request.POST.get('comment')
        answer = Answer(question=question, pick=pick, comment=comment)
        answer.save()

        return redirect(f'/eithers/{question_pk}/')
    else:
        return redirect(f'/eithers/{question_pk}/')


def comments_delete(request, answer_pk, question_pk):
    if request.method == 'POST':
        answer = Answer.objects.get(pk=answer_pk)
        answer.delete()
        return redirect(f'/eithers/{question_pk}/')
    else:
        return redirect(f'/eithers/{question_pk}/')