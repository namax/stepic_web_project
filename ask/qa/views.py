from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator, EmptyPage
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from qa.models import Question, Answer
from django.http import HttpResponse, Http404, HttpResponseRedirect
from qa.forms import AnswerForm, AskForm, SignupForm


def test(request, *args, **kwargs):
    return HttpResponse('OK', status=200)


def not_found(request, *args, **kwargs):
    return HttpResponse('Not Found', status=404)


def question_details(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    answers = Answer.objects.filter(question=question)
    form = AnswerForm(initial={'question': question.id})
    return render(request, 'qa/question_detail.html', {
        "question": question,
        "answers": answers.all(),
        "form": form,
        "title": "Question detail"
    })


def popular_questions_list(request):
    limit = 10
    questions = Question.objects.order_by("-rating")
    try:
        page_number = request.GET.get('page', 1)
    except ValueError:
        raise Http404
    paginator = Paginator(questions, limit)
    paginator.baseurl = "/?page="

    try:
        page = paginator.page(page_number)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)

    return render(request, 'qa/questions_list.html', {
        "questions": page.object_list,
        "paginator": paginator,
        "page": page,
        "title": "Popular questions"
    })


def last_questions_list(request):
    limit = 10
    questions = Question.objects.order_by("-id")
    try:
        page_number = request.GET.get('page', 1)
    except ValueError:
        raise Http404

    paginator = Paginator(questions, limit)
    paginator.baseurl = "/popular/?page="
    try:
        page = paginator.page(page_number)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)

    return render(request, 'qa/questions_list.html', {
        "questions": page.object_list,
        "paginator": paginator,
        "page": page,
        "title": "Last questions"
    })


def question_add(request):
    user = request.user
    if user.is_anonymous():
        return HttpResponseRedirect(reverse('login'))

    if request.method == 'POST':
        form = AskForm(request.POST)
        form.user = user
        if form.is_valid():
            question = form.save()

            return HttpResponseRedirect(reverse('question_details', kwargs={'question_id': question.id}))
    else:
        form = AskForm()

    return render(request, 'qa/question_add.html', {
        "form": form
    })


def save_answer(request):
    user = request.user
    if request.method == 'POST' and user.is_authenticated():
        form = AnswerForm(request.POST)
        form.user = user
        if form.is_valid():
            answer = form.save()
            return HttpResponseRedirect(reverse('question_details', kwargs={'question_id': answer.question.id}))

    return HttpResponseRedirect(reverse('login'))


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect(reverse('last_questions_list'))
    else:
        form = SignupForm()

    return render(request, 'registration/signup.html', {
        "form": form
    })
