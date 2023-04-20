



from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Question, Answer
from .forms import AnswerForm
from django.contrib.auth.models import User

def index(request):
    user = request.user.username
    context = {'user':user}
    return render(request,'index.html',context )

#@login_required  # Require user to be logged in
def answer_question(request, question_id):
    question = Question.objects.get(id=question_id)
    questtext = question.question_text
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer_text = form.cleaned_data['answer_text']
            answer = Answer(question=question, user=request.user, answer_text=answer_text)  # Link answer to user
            answer.save()
            return redirect('success_page')  # Redirect to a success page
    else:
        form = AnswerForm()
    return render(request, 'answer.html', {'form': form, 'question': question,'title':questtext})

def success_page(request):
    user = request.user.username
    context = {'user':user}
    return render(request, 'success_page.html',context)



#@login_required # use the login_required decorator to ensure the user is authenticated
def user_answers(request):
    user = request.user # retrieve the currently logged-in user
    user_answers = Answer.objects.filter(user=user) # retrieve all the answers made by the user
    context = {'user_answers': user_answers} # create a context dictionary with the user answers
    return render(request, 'user_answers.html', context) # render the user_answers.html template with the context dictionary


def organise_answers(request):
    user = request.user
    user_answers = Answer.objects.filter(user=user)
    
    quest1= user_answers.get(pk=3)
    quest2= user_answers.get(pk=4)
    quest3 = user_answers.get(pk=1)

    context = {'quest1':quest1,'quest2':quest2,'quest3':quest3}

    return render(request, 'sorted_answers.html',context)