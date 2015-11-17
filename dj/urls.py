from django.conf.urls import url
#from django.views.generic import TemplateView
from django.views.generic.base import TemplateView

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='dj_index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^your-name/$', views.get_name, name='your_name'),
    url(r'^thanks/$', TemplateView.as_view(template_name='dj/thanks.html'), name='thanks'),
]



"""
urlpatterns = [
    url(r'^$', views.index, name='dj_index'),
    # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
"""
