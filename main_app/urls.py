from django.urls import path
from django.contrib.auth.views import LogoutView

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('quiz/', views.quiz, name='quiz'),
    path('quiz/results', views.quiz_results, name='quiz_results'),
    path('questions/add', views.question_add, name='question_add'),
    path('questions/<int:question_id>/edit', views.question_edit, name='question_edit'),
    path('questions/<int:question_id>/delete', views.question_delete, name='question_delete'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('logout', LogoutView.as_view(), name='logout')
]