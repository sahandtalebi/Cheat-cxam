from django.shortcuts import render , redirect
from cheatexam_question.models import Question
from cheatexam_question.forms import QuestionForm


def homepage(request):
    question = Question.objects.all().order_by('-timestamp')

    context = {
        'question': question
    }
    return render(request, 'homepage.html', context)


def new_question(request, q=None):
    massage = request.GET.get('q')
    answer = request.GET.get('a')

    if massage:
        Question.objects.create(message=massage, answer=answer)




    return redirect('/')

def answer_question(request, **kwargs):
    id = (kwargs['id'])
    answer_the_question = request.GET.get('aq')
    if answer_the_question:
        Question.objects.filter(id=id).update(answer=answer_the_question)

    return redirect('/')


def delete_the_item(request , **kwargs):
    id = (kwargs["id"])
    delete_items = request.GET.get('dq')
    if delete_items:
        Question.objects.filter(id=id).delete()
    return redirect('/')

