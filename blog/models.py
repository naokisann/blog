from django.db import models
from django.utils import timezone
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify

class Category(models.Model):
    name = models.CharField("category name",max_length=255)
    created_at = models.DateTimeField('datetime',default=timezone.now)

    def __str__(self):
        return self.name


class Tag(models.Model): # add
    name = models.CharField("tag",max_length=50)
    created_at = models.DateTimeField("作成日",auto_now_add=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    """Post articles"""
    title  = models.CharField('title',max_length=50)
    subtitle = models.CharField('subtitle',max_length=100,blank=True)
    thumbnail = models.ImageField(upload_to='images/',blank=True)
    text = MarkdownxField('test_text')
    created_at = models.DateTimeField('datetime',default=timezone.now)
    category = models.ForeignKey(Category,verbose_name='category',on_delete=models.PROTECT)
    tag = models.ManyToManyField(Tag,blank=True,verbose_name='tag')
     # add
    def text_to_markdown(self):
        return markdownify(self.text)

    def get_previous_by_pk(self):
        """前のデータを取得する。"""
        return type(self).objects.filter(pk__lt=self.pk).last()

    def get_next_by_pk(self):
        """次のデータを取得する。"""
        return type(self).objects.filter(pk__gt=self.pk).first()



    def __str__(self):
        return self.title
