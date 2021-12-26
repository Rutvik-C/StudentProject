from django.shortcuts import render
from django.contrib.auth.decorators import login_required
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
    UpdateView,
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
    context_object_name = "Question"
    ordering = ["-date_posted"]


def QuestionDetailView(request, pk):
    context = {
        "question": Question.objects.filter(pk=pk).first(),
        "answers": Answer.objects.filter(question__pk=pk),
    }
    return render(request, "main/Question_detail.html", context)


def StudentQuestionListView(request, pk):
    context = {
        "student": Student.objects.filter(user__pk=pk).first(),
        "questions": Question.objects.filter(student__pk=pk),
    }
    print("in student")
    return render(request, "main/profile.html", context)


def StudentAnswerListView(request, pk):
    context = {
        "student": Student.objects.filter(user__pk=pk).first(),
        "answers": Answer.objects.filter(student__pk=pk),
    }
    print("in student")
    return render(request, "main/profile_ans.html", context)


class QuestionCreateView(LoginRequiredMixin, CreateView):
    model = Question
    fields = ["title", "description"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


def home_page(request):
    return render(request, "main/home.html")


def login_student(request):
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
        year = request.POST.get("g_year")
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

        new_user = User.objects.create_user(username=username, email=email, password=password)
        new_user.save()

        if University.objects.filter(name=university).exists():
            university_obj = University.objects.filter(name=university).first()

        else:
            university_obj = University(name=university)
            university_obj.save()

        new_student = Student(
            user=new_user,
            university=university_obj,
            graduation_year=year
        )
        new_student.save()

        login(request, new_user)

        return redirect("home-page")

    else:
        return render(request, "main/register.html")


def logout_student(request):
    logout(request)
    return redirect("home-page")


@login_required
def answer_question(request,question_pk):
    if request.method == "POST":
        description = request.POST.get("answer")

        new_ans = Answer.objects.create(description = description,student = request.user, question= Question.objects.filter(pk = question_pk).first(),date_posted = datetime.datetime.now())
        new_ans.save()

    return redirect("Questions-list-view")
    # redirect_to = "Question/" + str(question_pk) + "/"
    # return redirect(redirect_to)


def display_profile(request):
    context = {
        "student": Student.objects.filter(user__pk=pk).first(),
        "questions": Question.objects.filter(student__pk=pk),
    }
    print("in student")
    return render(request, "main/profile.html",context)