from django.conf.urls import url


from .views import (BookmarkCreateView,
                    BookmarkListView, BookmarkUpdateView,
                    BookmarkDeleteView, BookmarkDetail)

from .views import UserTags, UserFavorites, TagItems
from .views import AddFavorite
from pin import views
urlpatterns = [



    url(r'^$', BookmarkListView.as_view(), name="bookmarks"),

    url(r'^edit/(?P<bookmark_id>[0-9]+)/',
        BookmarkUpdateView.as_view(), name="edit_bookmark"),

    url(r'^detail/(?P<pk>[0-9]+)/',
        BookmarkDetail.as_view(), name="detail_bookmark"),

    url(r'^delete/(?P<pk>[0-9]+)/',
        BookmarkDeleteView.as_view(), name="delete_bookmark"),

    url(r'^add/', BookmarkCreateView.as_view(), name="add_bookmark"),



    # Users

    url(r'^tags/', UserTags.as_view(), name="user_tags"),
    url(r'^favorites/', UserFavorites.as_view(), name="user_favs"),

    # Favouriting


    url(r'^favorite/(?P<bookmark_id>\d+)/$',
        AddFavorite.as_view(), name="add_favorite"),

    url(r'^remove/favorite/(?P<bookmark_id>\d+)/$',
        views.delete_favorite, name="remove_favorite"),

    # Tags

    url(r'tag/(?P<tag>\w+)/$', TagItems.as_view(), name="tag_items"),

]
