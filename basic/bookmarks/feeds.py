from django.contrib.syndication.views import Feed
from models import Bookmark
from django.contrib.auth.models import User
import django.shortcuts as shortcuts

class LatestEntriesFeed(Feed):
    title = "Latest OER bookmarks"
    link = "/bookmarks/latest/feed/"
    description = "Latest OER bookmarks"

    def items(self):
        return Bookmark.objects.order_by('-created')[:10]

    def item_title(self, item):
        return item.url

    def item_description(self, item):
        return item.title
    
class LatestUserEntriesFeed(Feed):
    def get_object(self, request, user):
        return shortcuts.get_object_or_404(User, username=user)

    def title(self, obj):
        return "Latest OER bookmarks %s" % obj

    def link(self, obj):
        return "/bookmarks/user/"

    def description(self, obj):
        return "Latest OER bookmarks %s" % obj

    def items(self, obj):
        return Bookmark.objects.filter(user__id=obj.id).order_by('-created')[:10]

    def item_title(self, item):
        return item.url

    def item_description(self, item):
        return item.title
    