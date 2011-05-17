# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from osto.models import Barcode

def index(request):
	items = request.session.get('items', None)

	if items == None:
		items = request.session['items'] = []
	
	if request.method == 'POST' and request.POST['inputfield']:
		if request.POST['inputfield'] == 'CLEAR':
			items = request.session['items'] = []
		else:
			items.append(request.POST['inputfield'])
			request.session.modified = True
	
	items = [Barcode.get_or_code(x) for x in items]
	data = {'items': items[::-1]}
	return render_to_response('osto/index.html',
		data,
		context_instance=RequestContext(request))

