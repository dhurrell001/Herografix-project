from django.urls import path
from . import views



urlpatterns = [
    path("", views.index, name="index"),
    path('question/<int:question_id>/', views.answer_question, name='question_detail'),
    path('success_page', views.success_page, name='success_page'),
    path('user_answers', views.user_answers, name='user_answers'),
    path('sorted_answers', views.organise_answers, name='sorted_answers'),
    path('most_recent', views.most_recent_answer, name='most_recent'),
    path('tester', views.tester, name='tester'),
    path('display_answers', views.organise_answers, name='display_answers'),
   # path('grid_test', views.grid_test, name='grid_test'),
    path('index', views.index, name='index'),
   # path('test_2', views.test, name='test_2'),
    
    


]