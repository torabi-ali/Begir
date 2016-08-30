from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Download


def index(request):
    latest_download_list = Download.objects.order_by('-date')[:5]
    context = { 'latest_download_list': latest_download_list, }
    return render(request, 'download/index.html', context)

def detail(request, download_id):
    download = get_object_or_404(Download, pk=download_id)
    return render(request, 'download/detail.html', {'download': download})

def results(request, download_id):
    response = "You're looking at the results of DOWNLOAD %s."
    return HttpResponse(response % download_id)

def progress(request, download_id):
    return HttpResponse("You're processing DOWNLOAD %s." % download_id)
