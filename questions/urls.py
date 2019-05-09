from django.urls import path
from . import views

urlpatterns = [
    path('<int:question_id>/', views.question, name='question'),
    path('all/', views.all_questions, name='all-questions'),
    path('leaderboard/', views.leaderboard, name='leaderboard')
]
