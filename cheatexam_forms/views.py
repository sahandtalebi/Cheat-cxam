from django.shortcuts import render
from cheatexam_question.models import Question


def forms_view(request, *args, **kwargs):
    result = kwargs['slug']


    question = Question.objects.all().order_by('-timestamp')


    context = {
        'question': question,
    }
    return render(request, 'homepage.html', context)
