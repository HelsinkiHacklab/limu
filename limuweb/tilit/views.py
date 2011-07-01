# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from tilit.models import AccountCode

def show(request):
	account = AccountCode.get_or_code(x)
	data = {'account': account}
	return render_to_response('osto/account.html',
		data,
		context_instance=RequestContext(request))

def create(request):
	
