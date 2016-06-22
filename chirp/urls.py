
from django.conf.urls import url, include
from django.contrib import admin

from main.views import IndexView, ChirpDetailView, ChirpCreateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name="index_view"),
    url('^', include('django.contrib.auth.urls')),
    url(r'^chirp/(?P<pk>\d+)/$',ChirpDetailView.as_view(),name="chirp_detail_view"),
    url(r'^create_chirp/$', ChirpCreateView.as_view(),name="chirp_create_view"),
]
