from django.urls import path
from .views import (
    QuestionListView,
    QuestionDetailView,
    QuestionCreateView,
    HomePageView,
    QuestionUpdateView,
    QuestionDeleteView,
    AnswerCreateView,
    upvote_question,
    downvote_question,
)
from . import views

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("questions/", QuestionListView.as_view(), name="question_list"),
    path("create/", QuestionCreateView.as_view(), name="question_create"),
    path("<int:pk>/", QuestionDetailView.as_view(), name="question_detail"),
    path("<int:pk>/edit/", QuestionUpdateView.as_view(), name="question_edit"),
    path("<int:pk>/delete/", QuestionDeleteView.as_view(), name="question_delete"),
    path("<int:question_pk>/answer/", AnswerCreateView.as_view(), name="answer_create"),
    path("<int:pk>/comment_create/", views.comment_create, name="comment_create"),
    path("<int:pk>/upvote/", upvote_question, name="upvote_question"),
    path("<int:pk>/downvote/", downvote_question, name="downvote_question"),
]
