from django.shortcuts import render, redirect
from cheatexam_question.models import Question
from django.contrib.auth import get_user_model

User = get_user_model()


def homepage(request):
    ct = request.session.get('count', 0)
    new_count = ct + 1
    request.session['count'] = new_count
    question = Question.objects.all().order_by('-timestamp')


    context = {
        'question': question,
        'count': new_count,
    }
    return render(request, 'homepage.html', context)




def new_question(request, q=None):
    massage = request.GET.get('q')
    answer = request.GET.get('a')
    username = request.GET.get('username')
    username = User.objects.filter(username=username).first()
    if massage:
        Question.objects.create(message=massage, answer=answer, created_by=username)

    return redirect('/')


def answer_question(request, **kwargs):
    id = (kwargs['id'])
    answer_the_question = request.GET.get('aq')
    delete_the_question = request.GET.get('dq')

    if answer_the_question:
        Question.objects.filter(id=id).update(answer=answer_the_question)
    if delete_the_question:
        Question.objects.filter(id=id).delete()

    return redirect('/')


def delete_the_item(request , **kwargs):
    id = (kwargs["id"])
    delete_items = request.GET.get('dq')
    if delete_items:
        Question.objects.filter(id=id).delete()
    return redirect('/')

