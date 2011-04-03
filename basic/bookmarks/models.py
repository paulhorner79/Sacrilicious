from django.db import models
from django.utils.translation import ugettext_lazy as _
from tagging.fields import TagField
from tagging.models import Tag
from django.template.defaultfilters import slugify
from django.db.models import permalink
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
     

class Bookmark(models.Model):
    """Bookmarks model"""

    title = models.CharField(max_length=200, blank=True, null=True)
    slug = models.SlugField(_('slug'), unique=True)
    url = models.URLField(_('url'))
    description = models.TextField(_('description'), blank=True)

    extended = models.TextField(_('extended'), blank=True)
    created = models.DateTimeField(_('created'), auto_now_add=True)
    modified = models.DateTimeField(_('modified'), auto_now=True)

    license = models.URLField(blank=True)
    author = models.CharField(max_length=255, blank=True)
    publisher = models.CharField(max_length=255, blank=True)
    
    user = models.ForeignKey(User)
    
    keywords = TagField()

    class Meta:
        verbose_name = _('bookmark')
        verbose_name_plural = _('bookmarks')
        db_table = "bookmarks"

    def __unicode__(self):
        return self.url

    def get_absolute_url(self):
        return self.url

    def save(self, *args, **kwargs):
        self.slug = slugify("%s%s" % (self.title, self.user.id))
        super( Bookmark, self ).save(args, kwargs)

    def get_absolute_url(self):
        return reverse('basic.bookmarks.views.bookmark_detail', args=(self.created.year, self.created.strftime('%b').lower(), self.created.day, self.id))

    def _get_tags(self):
        return Tag.objects.get_for_object(self)
    
    def _set_tags(self, tag_list):
        Tag.objects.update_tags(self, tag_list)
    
    tags = property(_get_tags, _set_tags)
