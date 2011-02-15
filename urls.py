from django.conf.urls.defaults import *

# Usar somente no desenvolvimento
import os
APP_DIR = os.path.dirname( globals()[ '__file__' ] )
STATIC_PATH = os.path.join(APP_DIR, 'static')

urlpatterns = patterns('',
    # Usar somente no desenvolvimento
	(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': STATIC_PATH}),
    
	(r'^/?$', 'redirecionamento.views.adicionar'),
    (r'^(?P<id>[a-zA-Z0-9]+)/?$', 'redirecionamento.views.ir'),
    (r'^(?P<id>[a-zA-Z0-9]+)\+/?', 'redirecionamento.views.prever'),
)
