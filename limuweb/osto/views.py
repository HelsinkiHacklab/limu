# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext

def index(request):
	data = {}
	return render_to_response('osto/index.html',
		data,
		context_instance=RequestContext(request))

