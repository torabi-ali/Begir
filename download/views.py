from django.http import HttpResponse

from .models import Download

def index(request):
    latest_download_list = Download.objects.order_by('-date')[:5]
    output = ', '.join([d.link for d in latest_download_list])
    return HttpResponse(output)

def detail(request, question_id):
    return HttpResponse("You're looking at DOWNLOAD %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of DOWNLOAD %s."
    return HttpResponse(response % question_id)

def progress(request, question_id):
    return HttpResponse("You're processing DOWNLOAD %s." % question_id)
