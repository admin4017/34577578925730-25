from django.conf.urls import patterns, include, url
import views 

urlpatterns = patterns('',
	url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^info/$', views.InfoView.as_view(), name='info'),
	url(r'^stop_list/$', views.StopListView.as_view(), name='stop_list'),
	url('^googledc07046dcfeed7a4.html/$', views.GoogleView.as_view(), name='googledc07046dcfeed7a4.html'),
)
