



from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Question, Answer
from .forms import AnswerForm
from django.contrib.auth.models import User
from datetime import datetime

def index(request):
    user = request.user.username
    context = {'user':user}
    return render(request,'index.html',context )

def tester(request):
    return render(request,'tester.html')

#@login_required  # Require user to be logged in
def answer_question(request, question_id):
    question = Question.objects.get(question_identifier=question_id)
    questtext = question.question_text
    if request.method == 'POST': # runs if form has been filled in else it will render an empty form
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer_text = form.cleaned_data['answer_text']
            answer_date = datetime.now()
            answer = Answer(question=question, user=request.user, answer_text=answer_text,answer_date = answer_date)  # Link answer to user
            
            answer.save()
            return redirect('success_page')  # Redirect to a success page
    else:
        form = AnswerForm()
    return render(request, 'answer.html', {'form': form, 'question': question,'title':questtext})
 
# View to show succesfful completion of answer form
def success_page(request):
    user = request.user.username
    context = {'user':user}
    return render(request, 'success_page.html',context)



#@login_required # use the login_required decorator to ensure the user is authenticated
# list all answers submitted by current user
def user_answers(request):
    user = request.user # retrieve the currently logged-in user
    user_answers = Answer.objects.filter(user=user) # retrieve all the answers made by the user
    context = {'user_answers': user_answers} # create a context dictionary with the user answers
    return render(request, 'user_answers.html', context) # render the user_answers.html template with the context dictionary


def organise_answers(request):
    user = request.user
    user_answers = Answer.objects.filter(user=user) #get all Answer object for current user
    
    quest1= user_answers.get(question__question_identifier =3) # 'gets' and single object from aboce query set to allow for access of attributes in template
    quest2= user_answers.get(question__question_identifier =1)
    quest3 = user_answers.get(question__question_identifier =3)

    context = {'quest1':quest1,'quest2':quest2,'quest3':quest3}

    return render(request, 'sorted_answers.html',context)

def most_recent_answer(request):
    user = request.user   # gets current user data
    most_recent_answer = Answer.objects.filter(question__question_identifier =3, user=user).latest('answer_date') # geta answer object using current useer and  custom question id number
    context = {'most_recent': most_recent_answer}

    return render(request, 'most_recent.html',context)