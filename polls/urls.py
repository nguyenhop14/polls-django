from django.conf.urls import url

from polls.views import IndexView, DetailView, ResultsView
from . import views 

app_name = 'polls'
urlpatterns = [
  url(r'^$', IndexView.as_view(), name='index'),
  url(r'^(?P<pk>\d+)$', DetailView.as_view(), name='detail'),
  url(r'^(?P<pk>\d+)/results$', ResultsView.as_view(), name='results'),
  url(r'^ok$', views.note, name='note'),
  url(r'^(?P<question_id>\d+)/vote$', views.vote, name='vote')
]