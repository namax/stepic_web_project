from django.core.paginator import Paginator
from django.shortcuts import render
from qa.models import Question
# Create your views here.


from django.http import HttpResponse


def test(request, *args, **kwargs):
    return HttpResponse('OK', status=200)


def not_found(request, *args, **kwargs):
    return HttpResponse('Not Found', status=404)


def question_details(request, question_id):
    return HttpResponse(question_id)


def popular_questions_list(request):
    limit = 10
    questions = Question.objects.order_by("rating");
    pageNumber = request.GET.get('page', 1);
    paginator = Paginator(questions, limit)
    paginator.baseurl = "/?page="
    page = paginator.page(pageNumber)

    return render(request, 'qa/questions_list.html', {
        "questions": page.object_list,
        "paginator": paginator,
        "page": page,
        "title": "Last questions"
    })


def last_questions_list(request):
    limit = 10
    questions = Question.objects.order_by("-id");
    pageNumber = request.GET.get('page', 1);
    paginator = Paginator(questions, limit)
    paginator.baseurl = "/popular/?page="
    page = paginator.page(pageNumber)

    return render(request, 'qa/questions_list.html', {
        "questions": page.object_list,
        "paginator": paginator,
        "page": page,
        "title": "Last questions"
    })
