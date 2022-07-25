from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .forms import QuestionForm
from .models import Question

# Create your views here.

def home(request):
  return render(request, 'home.html')

@login_required
def quiz(request):
    questions = Question.objects.all()
    context = {'questions': questions}
    return render(request, 'quiz/quiz.html', context=context)

@login_required
def quiz_results(request):
    if request.method == 'POST':
        print(request.POST)
        questions = Question.objects.all()
        score = 0
        wrong = 0
        correct = 0
        total = 0
        for question in questions:
            total += 1
            question_answer = request.POST.get(str(question.id))
            answer_was_correct = question.answer == question_answer
            if answer_was_correct:
                score += 10
                correct += 1
            else:
                wrong += 1
        percent = score / (total * 10) * 100
        context = {
            'score': score,
            # 'time': request.POST.get('timer'),
            'correct': correct,
            'wrong': wrong,
            'percent': percent,
            'total': total
        }
        return render(request,'quiz/results.html', context)
    else:
        return redirect('home')

@login_required
def question_add(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'quiz/question_add.html', context)

@login_required
def question_edit(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            form.save()
            return redirect('quiz')
    else:
        form = QuestionForm(instance=question)
    context = {
        'form': form, 
        'question': question
    }
    return render(request, 'quiz/question_edit.html', context)
    
@login_required
def question_delete(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    question.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def register(request):
    if request.user.is_authenticated:
        return redirect('home') 
    else: 
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')
        else:
            form = UserCreationForm()
        context = {
            'form':form,
        }
        return render(request,'quiz/register.html', context)


def login_view(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request,'quiz/login.html')





