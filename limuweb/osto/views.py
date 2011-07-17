# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from osto.models import Barcode
from tilit.models import Account, AccountCode

def maybe_get_price(barcode):
    try:
        return barcode.product.current_price
    except AttributeError:
        return 0

def index(request):
    account = request.session.get('account', None)
    items = request.session.get('items', None)
    
    if items == None:
        items = request.session['items'] = []

    if request.method == 'POST' and request.POST['inputfield']:
        inputfield = request.POST['inputfield']
        if inputfield == 'Clear':
            items = request.session['items'] = []
            account = request.session['account'] = None
        elif inputfield == 'Accept':
            if isinstance(account,Account) and len(items) > 0:
                account.debit(sum([maybe_get_price(item) for item in items]))
                items = request.session['items'] = []
                account = request.session['account'] = None
        else: 
            if account:
                items.append(inputfield)
                request.session.modified = True
            else:
                account = request.session['account'] = inputfield
                request.session.modified = True
    
    account = AccountCode.get_or_code(account)
    items = [Barcode.get_or_code(x) for x in items]
    data = {'account': account, 'items': items[::-1], 'total' : sum([maybe_get_price(item) for item in items])}
    return render_to_response('osto/index.html',
        data,
        context_instance=RequestContext(request))

