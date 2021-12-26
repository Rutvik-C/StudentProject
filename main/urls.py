from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *


urlpatterns = [
    path("", home_page, name="home-page"),
    path("login", login_student, name="login"),
    path("register", register_student, name="register"),
    path("answers/<int:question_pk>/", answer_question, name="answers"),
    path("profile", display_profile, name="profile"),
    path("logout", logout_student, name="logout"),
    path("Questions", QuestionListView.as_view(), name="Questions-list-view"),
    path("Question/<int:pk>/", QuestionDetailView, name="Questions-detail"),
    path(
        "Student/question/<int:pk>/",
        StudentQuestionListView,
        name="Student-question-list",
    ),
    path(
        "Student/answer/<int:pk>/",
        StudentAnswerListView,
        name="Student-answer-list",
    ),
    # path('about/', views.about, name="books-about"),
]

# path('Question/new/', QuestionCreateView.as_view(), name="Questions-create"),
# path('Question/<int:pk>/update/', QuestionUpdateView.as_view(), name="Questions-update"),
# path('Question/<int:pk>/delete/', QuestionDeleteView.as_view(), name="Questions-delete"),
# path('Question/search/', views.search, name="Questions-search"),
