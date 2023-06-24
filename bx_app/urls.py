from django.urls import path, include
from . import views
from django.contrib import admin

from accounts import views as accounts_views



from django.contrib.auth import views as auth_views

from accounts import views as accounts_views


urlpatterns = [
    path("", views.index, name="index"),
    path('question/<int:question_id>/', views.answer_question, name='question_detail'),
    path('success_page', views.success_page, name='success_page'),
    path('user_answers', views.user_answers, name='user_answers'),
    path('sorted_answers', views.organise_answers, name='sorted_answers'),
    path('most_recent', views.most_recent_answer, name='most_recent'),
   # path('tester', views.tester, name='tester'),
    path('tester/<int:question_id>/', views.tester, name='question_detail'),
    path('display_answers', views.organise_answers, name='display_answers'),
   # path('grid_test', views.grid_test, name='grid_test'),
    path('index', views.index, name='index'),
    path('test', views.test, name='test'),
    path('signup', accounts_views.signup, name='signup'),
    path('admin', admin.site.urls),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('login', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('accounts/', include('django.contrib.auth.urls'))
   
   
    
    
    


]