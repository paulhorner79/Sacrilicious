from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
import settings
from django.contrib.auth import views as auth_views

admin.autodiscover()

urlpatterns = patterns('',
     url(r'^admin/', include(admin.site.urls)),
     (r'^bookmarks/', include('basic.bookmarks.urls')),
     url(r'^auth/', include('social_auth.urls')),
     url(r'^auth/logout/$',
       auth_views.logout,
       {'template_name': 'auth/logout.html'},
       name='auth_logout'),

)

if settings.DEBUG:
    urlpatterns += patterns("",
                            url(r'media/(?P<path>.*)$','django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
            )
