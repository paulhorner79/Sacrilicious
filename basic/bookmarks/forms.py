from django import forms
import models

class BookmarkForm(forms.ModelForm):
    class Meta:
        model = models.Bookmark
        fields = ('title','url','description','publisher','author', 'license','keywords')
