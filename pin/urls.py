from django.conf.urls import url


from .views import (BookmarkCreateView,
                    BookmarkListView, BookmarkUpdateView,
                    BookmarkDeleteView)

from .views import UserTags, UserFavorites, TagItems
from .views import AddFavorite

urlpatterns = [



    url(r'^$', BookmarkListView.as_view(), name="bookmarks"),

    url(r'^edit/(?P<pk>[0-9]+)/',
        BookmarkUpdateView.as_view(), name="edit_bookmark"),

    url(r'^delete/(?P<pk>[0-9]+)/',
        BookmarkDeleteView.as_view(), name="delete_bookmark"),

    url(r'^add/', BookmarkCreateView.as_view(), name="add_bookmark"),

    url(r'^tags/', UserTags.as_view(), name="user_tags"),
    url(r'^favorites/', UserFavorites.as_view(), name="user_favs"),


    url(r'^add_fav/(?P<bookmark_id>\d+)/$',
        AddFavorite.as_view(), name="add_favorite"),

    url(r'tag/(?P<tag>\w+)/$', TagItems.as_view(), name="tag_items"),

]
