from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.utils import simplejson
from redirecionamento.models import Endereco, EnderecoForm

def ir(request, id):
    endereco = get_object_or_404(Endereco, codigo = id)
    return HttpResponsePermanentRedirect(endereco.destino)

def adicionar(request):
    if request.method == 'POST':
        form = EnderecoForm(request.POST)
        try:
            encurtamento = Endereco.objects.get(destino = request.POST['destino'])
            response = {'codigo': encurtamento.codigo, 'destino': encurtamento.destino}
        except Endereco.DoesNotExist:
            if form.is_valid():
                encurtamento = form.save()
                response = {'codigo': encurtamento.codigo, 'destino': encurtamento.destino}
            else:
                response = {'erro': True}
        json = simplejson.dumps(response, ensure_ascii = False)
        return HttpResponse(json, mimetype = "application/json")
    else:
        form = EnderecoForm()
    return render_to_response('redirecionamento/adicionar.html', {'form': form}, context_instance = RequestContext(request))

def prever(request, id):
    endereco = get_object_or_404(Endereco, codigo = id)
    return render_to_response('redirecionamento/prever.html', {'endereco': endereco})