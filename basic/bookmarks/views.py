from django.views.generic import date_based, list_detail
import django.http as http
import django.shortcuts as shortcuts
import django.template.context as context
from basic.bookmarks.models import *
import forms
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from tagging.models import TaggedItem, Tag


@login_required
def user_bookmark_list(request, page=0):
    return bookmark_list(request,page,user=True)

def bookmark_list(request, page=0,user=False):
    objects = Bookmark.objects.all()
    ext = {}
    
    if user:
        objects = objects.filter(user__id=request.user.id)
    else:
        ext['view_all'] = True
    
    return list_detail.object_list(
        request,
        queryset=objects,
        paginate_by=20,
        page=page,
        extra_context = ext
    )
bookmark_list.__doc__ = list_detail.object_list.__doc__
def bookmark_detail(request, object_id, year, month, day):
    return date_based.object_detail(
        request,
        year=year,
        month=month,
        day=day,
        date_field='created',
        object_id=object_id,
        queryset=Bookmark.objects.all(),
    )
bookmark_detail.__doc__ = date_based.object_detail.__doc__

def bookmark_detail(request, object_id, year, month, day):
    return date_based.object_detail(
        request,
        year=year,
        month=month,
        day=day,
        date_field='created',
        object_id=object_id,
        queryset=Bookmark.objects.all(),
    )
bookmark_detail.__doc__ = date_based.object_detail.__doc__

def bookmarks_by_tag(request, tag, page=0):
    tag = Tag.objects.get(name=tag)
    return list_detail.object_list(
        request,
        queryset=TaggedItem.objects.get_by_model(Bookmark, tag),
        paginate_by=20,
        page=page,
        extra_context = {'tag': tag}
    )
bookmark_list.__doc__ = list_detail.object_list.__doc__


@login_required
def bookmark_add(request):
    bag = {}
    
    if request.method == 'POST': 
        form = forms.BookmarkForm(request.POST) 
        if form.is_valid(): 
            
            bookmark = form.save(commit=False)
            bookmark.user = request.user
            bookmark.save()

            messages.add_message(request, messages.INFO, 'Bookmark added!')            
            return http.HttpResponseRedirect(bookmark.url) 
    else:
        
        form = forms.BookmarkForm() 
        form.fields['url'].initial = request.GET.get('url', '')
        form.fields['title'].initial = request.GET.get('title', '')
        form.fields['publisher'].initial = request.GET.get('publisher', '')
        form.fields['author'].initial = request.GET.get('author', '')
        form.fields['license'].initial = request.GET.get('license', '')

    bag['form'] = form
    
    return shortcuts.render_to_response("bookmarks/add.html", 
                                        bag, 
                                        context_instance=context.RequestContext(request))
