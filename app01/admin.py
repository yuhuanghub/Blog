from django.contrib import admin
from  app01.models import Article

class AriticleList(admin.ModelAdmin):
    list_display = ('title','category',)

# Register your models here.
admin.site.register(Article,AriticleList)
