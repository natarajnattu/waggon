from django.shortcuts import redirect, get_object_or_404, render
from django.views.generic import (DeleteView, UpdateView,
                                  TemplateView, ListView,
                                  DetailView, View)
# from django.core.urlresolvers import reverse
from .models import Bookmark, Favorite
from .forms import BookmarkForm
from taggit.models import Tag
from braces import views
from django.db import IntegrityError
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse


class BookmarkListView(views.LoginRequiredMixin, ListView):
    model = Bookmark
    template_name = "pin/index.html"

    def get_queryset(self):
        return Bookmark.objects.filter(user=self.request.user.id)

    def get_context_data(self, **kwargs):
        context = super(BookmarkListView, self).get_context_data(**kwargs)
        context['popular_user_tags'] = Tag.objects.filter(
            bookmark__user=self.request.user.id)
        return context


class BookmarkCreateView(views.LoginRequiredMixin, View):

    def get(self, request):
        form = BookmarkForm()
        return render(request, 'pin/edit.html', {'form': form})

    # This POST should be the fastest :( too slow;
    # Get this down to milliseconds

    def post(self, request):
        form = BookmarkForm(data=request.POST)
        if form.is_valid():
            url = form.cleaned_data['link']
            try:
                object = form.save(commit=False)
                from bs4 import BeautifulSoup
                import requests
                response = requests.get(url)
                BeautifulSoup(response.content)
                object.title = BeautifulSoup(response.content).find('title').text
                object.user_id = request.user.id
                object.save()
                form.save_m2m()
                return redirect("bookmarks")

            except IntegrityError:
                return HttpResponse("Bookmark Already Exists")


class BookmarkDetail(views.LoginRequiredMixin, DetailView):
    model = Bookmark
    template_name = "pin/detail.html"
    context_object_name = "bookmark"


class BookmarkUpdateView(views.LoginRequiredMixin, UpdateView):
    success_url = "/"
    form_class = BookmarkForm
    model = Bookmark
    template_name = 'pin/edit.html'

    def form_valid(self, form):
        return super(BookmarkUpdateView, self).form_valid(form)

    def dispatch(self, *args, **kwargs):
        if self.request.user.pk == self.get_object().user.pk:
            return super(BookmarkUpdateView, self).dispatch(*args, **kwargs)
        else:
            raise PermissionDenied


class IsReadBook():
    pass


class BookmarkDeleteView(views.LoginRequiredMixin, DeleteView):
    model = Bookmark
    success_url = '/'

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)


class UserTags(views.LoginRequiredMixin, ListView):
    context_object_name = 'tags'
    template_name = 'pin/tags.html'

    def get_queryset(self):
        return Tag.objects.filter(bookmark__user=self.request.user.id)


class UserFavorites(views.LoginRequiredMixin, ListView):
    context_object_name = 'favorites'
    template_name = 'pin/favorites.html'

    def get_queryset(self):
        return Favorite.objects.filter(user__pk=self.request.user.id)

# Future Implementation


class UserDashBoard(views.LoginRequiredMixin, TemplateView):
    pass


class TagItems(View):

    def get(self, request, tag):
        bookmarks = Bookmark.objects.filter(
            tags__name=tag, user=request.user.id)
        return render(request, 'pin/index.html', {'object_list': bookmarks})


class AddFavorite(views.LoginRequiredMixin, View):

    def get(self, request, bookmark_id):
        # TODO: this should probably be a POST action
        bookmark = get_object_or_404(Bookmark, pk=bookmark_id)
        try:
            Favorite.objects.get(
                user=request.user,
                bookmark=bookmark)
        except Favorite.DoesNotExist:
            Favorite.objects.create(
                user=request.user,
                bookmark=bookmark)
        return redirect('bookmarks')


def delete_favorite(request, bookmark_id):
    favorite = get_object_or_404(Favorite,
                                 bookmark__pk=bookmark_id,
                                 user=request.user)
    if request.method == 'POST':
        favorite.delete()
        return redirect('bookmarks')
    else:
        return render(request, 'pin/confirm_bookmark_delete.html',
                      {'bookmark': favorite.bookmark})
