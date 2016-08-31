from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'download/index.html')


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of DOWNLOAD %s."
    return HttpResponse(response % question_id)


def progress(request, question_id):
    return HttpResponse("You're processing DOWNLOAD %s." % question_id)
