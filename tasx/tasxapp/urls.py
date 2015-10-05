from django.conf.urls import include, url
from . import views

urlpatterns = [
    ##url(r'^$', views.index, name='index'),
    url(r'^$', views.index),
    url(r'^report/(?P<pk>[0-9]+)/$', views.report_detail, name='report_detail'),
    ##url(r'^post/new/$', views.new_report, name='new_report'),

]
