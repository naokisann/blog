from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin # ドラッグ&ドロップで画像を読み込む
from .models import Post,Category,Tag



admin.site.register(Post,MarkdownxModelAdmin)
admin.site.register(Category)
admin.site.register(Tag)
