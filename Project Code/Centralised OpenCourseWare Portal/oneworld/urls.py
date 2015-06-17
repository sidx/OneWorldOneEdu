from django.conf.urls import patterns, include, url

from django.conf import settings
from django.conf.urls.static import static
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'app.views.homepage', name='home'),
    # url(r'^oneworld/', include('oneworld.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^ratings/', include('ratings.urls')),
    
    url(r'^search/', include('search.urls', namespace='Search')),
    url(r'^login/',include('login.urls', namespace='Login')),
    url(r'^about/', 'app.views.aboutpage', name='about'),
    url(r'^panel/', 'app.views.t_login', name='panel'),

)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
     
