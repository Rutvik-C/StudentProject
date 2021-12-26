from django.shortcuts import render
from .models import * 
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    UpdateView
)
# Create your views here.

# class UserQuestionListView(ListView):
#     model = Question
#     template_name = 'Questions/user_Questions.html'  # <app>/<model>_<viewtype>.html
#     context_object_name = 'Question'
#     ordering = ['-date_posted']
#     paginate_by = 5

#     def get_queryset(self):
#         user = get_object_or_404(User, username=self.kwargs.get(
#             'username'))  # gets the username from url
#         return Question.objects.filter(user=user).order_by("price")


class QuestionListView(ListView):
    model = Question
    template_name = 'Questions/home2.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'Question'
    ordering = ['-date_posted']
    paginate_by = 5

class QuestionDetailView(DetailView):
    model = Question
