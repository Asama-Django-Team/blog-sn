from django.contrib import admin
from .models import Article
# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "publish", "status")
    list_filter = ("publish", "status")
    search_fields = ("title", "description")
    #prepopulated_fields = {}
    ordering = ('-publish',)



admin.site.register(Article, ArticleAdmin)