from django.contrib import admin
from .models import *

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'is_published', 'created_at')


admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Contact)
admin.site.register(Subscribe)
admin.site.register(About)
admin.site.register(Comment)
