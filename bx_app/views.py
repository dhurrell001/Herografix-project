



from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Question, Answer
from .forms import AnswerForm
from django.contrib.auth.models import User
from datetime import datetime
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.utils import timezone

def index(request):
    user = request.user
    context = {'user':user}
    return render(request,'index.html',context )

def tester(request):
    return render(request,'quest_revamp.html')

def grid_test(request):
    return render(request,'grid_css_test.html')

def test(request):
    return render(request,'login.html')



@login_required  # Require user to be logged in
def answer_question(request, question_id):
    max_quetion = 3
    if question_id <= max_quetion:
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
            #change back to answer.html if messing around does not work!!
        return render(request, 'quest_revamp.html', {'form': form, 'question': question,'title':questtext})
    else:
        return redirect('success_page')
 
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
    # get the latest answer to question. filter by id and onlt store results in 1 item list [:1]. check if this item exist else replace with None
    # order of how they are displayed can be rearranged in display_answers.html
    try:
        user = request.user
        subquery1 = Answer.objects.filter(user=user, question__question_identifier=1).order_by('-answer_date')[:1]
        subquery2 = Answer.objects.filter(user=user, question__question_identifier=2).order_by('-answer_date')[:1]
        subquery3 = Answer.objects.filter(user=user, question__question_identifier=3).order_by('-answer_date')[:1]
        
        quest1= subquery1[0] if subquery1 else None
        quest2= subquery2[0] if subquery2 else None
        quest3 = subquery3[0] if subquery3 else None

        context = {'quest1':quest1,'quest2':quest2,'quest3':quest3}

        return render(request, 'display_answers.html',context)
    
    except Exception as e:
        # return an error message
        return HttpResponse("An error occurred: " + str(e))

def most_recent_answer(request):
    user = request.user   # gets current user data
    most_recent_answer = Answer.objects.filter(question__question_identifier =1, user=user).latest('answer_date') # geta answer object using current useer and  custom question id number
    context = {'most_recent': most_recent_answer}

    return render(request, 'most_recent.html',context)



