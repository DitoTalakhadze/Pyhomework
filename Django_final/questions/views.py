from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Question, Tag, Answer, Vote
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.http import HttpResponseForbidden
from .forms import CommentForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django import forms
from django.db.models import Q


class HomePageView(View):
    def get(self, request):
        question_list_url = reverse("question_list")
        return render(request, "home.html", {"question_list_url": question_list_url})


class QuestionListView(ListView):
    model = Question
    template_name = "question_list.html"
    context_object_name = "questions"
    ordering = ["-id"]

    def get_queryset(self):
        query = self.request.GET.get("q")
        if query:
            # Filter questions by title or tags containing the search query
            return Question.objects.filter(
                Q(title__icontains=query) | Q(tags__name__icontains=query)
            ).distinct()
        else:
            return Question.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_query"] = self.request.GET.get("q", "")
        return context


class QuestionDetailView(DetailView):
    model = Question
    template_name = "question_detail.html"
    context_object_name = "question"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        question = self.get_object()
        context["answers"] = question.answer_set.all()
        context["form"] = CommentForm()
        return context


class QuestionCreateView(LoginRequiredMixin, CreateView):
    model = Question
    template_name = "question_create.html"
    fields = ["title", "body", "tags"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tags"] = Tag.objects.all()
        return context


class QuestionUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Question
    fields = ("title", "body", "tags")
    template_name = "question_edit.html"

    def test_func(self):
        question = self.get_object()
        return self.request.user == question.author

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tags"] = Tag.objects.all()
        return context


class QuestionDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Question
    template_name = "question_delete.html"
    success_url = reverse_lazy("home")

    def test_func(self):
        question = self.get_object()
        return self.request.user == question.author


class AnswerCreateView(LoginRequiredMixin, CreateView):
    model = Answer
    template_name = "answer_create.html"
    fields = ["body"]

    def form_valid(self, form):
        question = get_object_or_404(Question, pk=self.kwargs["question_pk"])

        if question.author == self.request.user:
            return HttpResponseForbidden(
                "You are not allowed to answer your own question."
            )

        form.instance.question = question
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        question = get_object_or_404(Question, pk=self.kwargs["question_pk"])
        context["question"] = question
        return context

    def get_success_url(self):
        return reverse_lazy(
            "question_detail", kwargs={"pk": self.kwargs["question_pk"]}
        )


@login_required
def comment_create(request, pk):
    question = get_object_or_404(Question, pk=pk)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.question = question
            comment.author = request.user  # Set the logged-in user as the author
            comment.save()
            messages.success(request, "Comment added successfully.")
            return redirect(question.get_absolute_url())
    else:
        form = CommentForm()

    form.fields["author"].widget = forms.HiddenInput()

    return render(request, "comment_create.html", {"form": form})


@login_required
def upvote_question(request, pk):
    question = get_object_or_404(Question, pk=pk)
    question.upvote(request.user)
    return redirect("question_detail", pk=pk)


@login_required
def downvote_question(request, pk):
    question = get_object_or_404(Question, pk=pk)
    question.downvote(request.user)
    return redirect("question_detail", pk=pk)
