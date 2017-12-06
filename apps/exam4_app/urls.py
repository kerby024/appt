from django.conf.urls import url
from . import views
urlpatterns = [
        url(r'^display$', views.display),
        url(r'^newappt$', views.newappt),
        url(r'^appt/(?P<apptid>\d+)$', views.update),
        url(r'^process/(?P<apptid>\d+)$', views.process),
        url(r'^appt/(?P<apptid>\d+)/delete$', views.delete),
        url(r'^clear$', views.clear),
]