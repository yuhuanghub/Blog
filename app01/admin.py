from django.contrib import admin
from  app01.models import Article
from pagedown.widgets import AdminPagedownWidget
from django import forms

class ArticleForm(forms.ModelForm):
    content = forms.CharField(widget=AdminPagedownWidget())
    class Meta:
        model = Article
        fields = '__all__'

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category',)
    form = ArticleForm

admin.site.register(Article,ArticleAdmin)
# # Register your models here.
# admin.site.register(Article)

