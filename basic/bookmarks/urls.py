from django.conf.urls.defaults import *
from feeds import LatestEntriesFeed, LatestUserEntriesFeed
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = patterns('basic.bookmarks.views',
    url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/(?P<object_id>\d+)/$',
        view='bookmark_detail',
        name='bookmark_detail',
    ),

    url(r'^all/$',
        view='bookmark_list',
        name='bookmark_index',
    ),
    
    url(r'^$',
        view='user_bookmark_list',
        name='user_bookmark_index',
    ),

    url(r'^add/$',
        view='bookmark_add',
        name='bookmark_add',
    ),

    url(r'^by_tag/(?P<tag>.*)/$',
        view='bookmarks_by_tag',
        name='bookmarks_by_tag',
    ),

)

urlpatterns += patterns('',
    (r'^latest/feed/$', LatestEntriesFeed()),
    (r'^latest/user/(?P<user>.*)/feed/$', LatestUserEntriesFeed()),
)
urlpatterns += staticfiles_urlpatterns()
