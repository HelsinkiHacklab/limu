# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext

def index(request):
	items = request.session.get('items', None)

	if items == None:
		items = []
	
	if request.method == 'POST' and request.POST['inputfield']:
		if request.POST['inputfield'] == 'CLEAR':
			items = []
		else:
			items.append(request.POST['inputfield'])
	
	request.session['items'] = items
	
	data = {'items': items[::-1]}
	return render_to_response('osto/index.html',
		data,
		context_instance=RequestContext(request))

