from django import forms
from .models import Bookmark
from taggit.forms import TagWidget


class BookmarkForm(forms.ModelForm):

    def full_clean(self):
        super(BookmarkForm, self).full_clean()
        try:
            self.instance.validate_unique()
        except forms.ValidationError as e:
            self._update_errors(e)

    class Meta:
        model = Bookmark
        fields = ('link', 'title', 'description', 'tags')
        widgets = {
            'tags': TagWidget(),
        }
