from django.shortcuts import render
from .models import * 
from django.http import HttpResponse
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
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
#         user = get_object_or_s404(User, username=self.kwargs.get(
#             'username'))  # gets the username from url
#         return Question.objects.filter(user=user).order_by("price")


class QuestionListView(ListView):
    model = Question
    # <app>/<model>_<viewtype>.html
    context_object_name = 'Question'
    ordering = ['-date_posted']



def QuestionDetailView(request,pk):
    context = {
        'question': Question.objects.filter(pk = pk).first(),
        'answers': Answer.objects.filter(question__pk =pk)
    }
    return render(request, 'main/Question_detail.html', context)

def StudentQuestionListView(request,pk):
    context = {
        'student': Student.objects.filter(user__pk =pk).first(),
        'questions': Question.objects.filter(student__pk =pk),
    }
    print("in student")
    return render(request, 'main/Student_Question_detail.html', context)

class QuestionCreateView(LoginRequiredMixin, CreateView):
    model = Question
    fields = ['title', 'description']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


def home_page(request):
    return render(request, "main/base.html")
    

def login_student(request, username, password):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home-page")

        else:
            messages.error(request, "Invalid credentials")
            return redirect("login")

    else:
        return render(request, "main/login.html")


def register_student(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        university = request.POST.get("university")
        password = request.POST.get("password")
        password_again = request.POST.get("confirm_password")

        if password != password_again:
            messages.error(request, "Passwords do not match")
            return redirect("register")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username taken")
            return redirect("register")

        if User.objects.filter(email=email).exists():
            messages.error(request, "E-Mail taken")
            return redirect("register")

        # Here

    else:
        return render(request, "main/register.html")


def logout_student(request):
    logout(request)
    return redirect("home-page")

