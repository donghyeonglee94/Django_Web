from django.shortcuts import render
from django.views.generic import ListView, DeleteView
from bookmark.models import Bookmark

class BookmarkLV(ListView):
    model = Bookmark
    context_object_name = 'object_list'
    template_name = 'bookmark/bookmark_list.html'

class BookmarkDV(DeleteView):
    model = Bookmark
    context_object_name = 'object'
    template_name = 'bookmark/bookmark_detail.html'