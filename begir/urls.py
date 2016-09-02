from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.views.generic import RedirectView

urlpatterns = [
#    url(r'^/', RedirectView.as_view(url='/download/index')),
    url(r'^admin/', admin.site.urls),
    url(r'^download/', include('download.urls')),
#    url('^register/', CreateView.as_view(template_name='register.html', form_class=UserCreationForm, success_url='/')),
#    url('^accounts/', include('django.contrib.auth.urls')),
]