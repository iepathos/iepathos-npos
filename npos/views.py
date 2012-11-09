from django.shortcuts import render
from django.views.generic import DetailView, ListView

from npos.models import Npo

class NpoListView(ListView):
	template_name = 'npos/index.html'

	def get_queryset(self):
		npos = Npo.active.all()
		return npos

class NpoDetailView(DetailView):
	model = Npo
	template_name = 'npos/detail.html'
