from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from download import models
from .models import Download


class IndexView(generic.ListView):
    model = Download
    template_name = 'download/index.html'


class DetailView(generic.DetailView):
    model = Download
    template_name = 'download/detail.html'


class ResultsView(generic.DetailView):
    model = Download
    template_name = 'download/results.html'


def progress(request, download_link):
    download = models.Download(link=download_link, status = 0)
    download.save()
    return HttpResponseRedirect(reverse('download:detail', args=(download.id,)))