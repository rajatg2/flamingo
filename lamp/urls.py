from django.conf.urls import patterns, url

from lamp import views

urlpatterns = patterns('',
    # ex: /lamp/
    url(r'^$', views.index, name='index'),
    url(r'^initialsubmission$', views.initialsubmission, name='initialsubmission'),
    url(r'^submission$', views.submission, name='submission'),
    url(r'^edited$', views.edited, name='edited'),

    # ex: /polls/5/
    #url(r'^specifics/(?P<question_id>\d+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    #url(r'^(?P<question_id>\d+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    #url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),   
)    