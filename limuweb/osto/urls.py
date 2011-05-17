from django.conf.urls.defaults import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    (r'^$', 'limuweb.osto.views.index'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
