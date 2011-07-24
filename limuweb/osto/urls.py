from django.conf.urls.defaults import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    (r'^$', 'limuweb.osto.views.index'),
    (r'^new_account$', 'limuweb.osto.views.new_account')
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
