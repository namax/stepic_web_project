from django.core.paginator import Paginator, EmptyPage
from django.shortcuts import render, get_object_or_404
from qa.models import Question, Answer
from django.http import HttpResponse, Http404


def test(request, *args, **kwargs):
    return HttpResponse('OK', status=200)


def not_found(request, *args, **kwargs):
    return HttpResponse('Not Found', status=404)


def question_details(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    answers = Answer.objects.filter(question=question)
    return render(request, 'qa/question_detail.html', {
        "question": question,
        "answers": answers.all(),
        "title": "Question detail"
    })


def popular_questions_list(request):
    limit = 10
    questions = Question.objects.order_by("rating")
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
