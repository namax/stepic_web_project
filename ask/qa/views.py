from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def question_details(request, question_id):
    return HttpResponse(question_id)


def not_found(request, *args, **kwargs):
    return HttpResponse('Not Found', status=404)
