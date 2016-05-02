from django import forms
from .models import Bookmark
from taggit.forms import TagWidget


class BookmarkForm(forms.ModelForm):
    """
    def full_clean(self):
        super(BookmarkForm, self).full_clean()
        try:
            self.instance.validate_unique()
        except forms.ValidationError as e:
            self._update_errors(e)

    def validate_unique(self):
        exclude = self._get_validation_exclusions()
        exclude.remove('user')  # allow checking against the missing attribute

        try:
            self.instance.validate_unique(exclude=exclude)
        except forms.ValidationError as e:
            self._update_errors(e.message_dict)
    """
    class Meta:
        model = Bookmark
        exclude = ('user', 'title')
        widgets = {
            'tags': TagWidget(),
        }
