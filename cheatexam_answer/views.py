from django.shortcuts import render
from cheatexam_question.models import Question

# Create your views here.

def answerquestion(request):
    answer = Question.objects.all().filter(iknow=True)
    context = {
        'answer': answer
    }
    return render(request, 'homepage.html', context)



