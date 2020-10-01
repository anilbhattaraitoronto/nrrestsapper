from django.contrib import admin

from .models import Topic, Post


class TopicAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',), }


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category',
                    'archived', 'new', 'featured', 'posted_date']
    list_editable = ['archived', 'featured', 'new']
    list_filter = ['author', 'category', 'archived', 'new', 'featured']
    prepopulated_fields = {'slug': ('title', ), }


admin.site.register(Topic, TopicAdmin)
admin.site.register(Post, PostAdmin)
