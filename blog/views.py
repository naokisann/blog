from django.views import generic
from django.shortcuts import get_object_or_404
from .models import Post,Category,Tag
from django.db.models import Q #　記事の内容を検索するためのパッケージ

class IndexView(generic.ListView):
    model = Post
    paginate_by = 2

    def get_queryset(self):
        queryset = Post.objects.order_by('-created_at')#
        keyword = self.request.GET.get('keyword')#検索フォームからの入力内容を取得
        if keyword:
            #queryset = queryset.filter(title = keyword) 検索内容と記事名が完全に一致する場合
            queryset = queryset.filter( Q(title__icontains = keyword)|Q(text__icontains = keyword))
            # text_icontains...記事の内容を検索する時に使用
        return queryset

class CategoryView(generic.ListView):
    model = Post
    paginate_by = 10
    def get_queryset(self):
        category = get_object_or_404(Category,pk=self.kwargs['pk'])
        queryset = Post.objects.order_by('-created_at').filter(category=category)
        return queryset


class DetailView(generic.DetailView):
    model = Post


class TagView(generic.ListView):
    """タグのリンククリック"""

    def get_queryset(self):
        """タグで絞り込み"""
        tag_name = self.kwargs['tag']
        self.tag = Tag.objects.get(name=tag_name)
        queryset = Post.objects.order_by('-created_at').filter(tag=self.tag)
        return queryset
