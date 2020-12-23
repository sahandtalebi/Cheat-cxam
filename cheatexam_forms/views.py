from django.shortcuts import render
from cheatexam_question.models import Question

def forms_view(request, *args, **kwargs):

    result = kwargs['slug']
    ct = request.session.get('count', 0)
    new_count = ct + 1
    request.session['count'] = new_count

    question = Question.objects.all().order_by('-timestamp')

    context = {
        'question': question,
        'count': new_count,
    }
    return render(request, 'homepage.html', context)
