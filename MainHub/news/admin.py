from django.contrib import admin

# Register your models here.
from .models import Article
# Register your models here.
# admin.site.register(Slider)
@admin.register(Article)
class adminArticle(admin.ModelAdmin):
    list_display = ['title','status']
    search_fields = ['title','status']
    date_hierarchy = 'created_at'
    prepopulated_fields = {'slug':['title']}
    list_per_page = 2
