from django.conf.urls import patterns, include, url

from npos.views import NpoDetailView, NpoListView

urlpatterns = patterns('npos.views',
	url(r'^npo/(?P<name>[-\w]+)/$', NpoDetailView.as_view(), name='npos_npo_detail'),
	url(r'^$', NpoListView.as_view(), name='npos_npo_index'),
)
