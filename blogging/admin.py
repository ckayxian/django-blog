from django.contrib import admin

# Register your models here.
from blogging.models import Post, Category


class CategoryAdmin(admin.ModelAdmin):
    exclude = ('posts',)
admin.site.register(Category, CategoryAdmin)

class CategoryInline(admin.TabularInline):
    model = Category.posts.through

class PostAdmin(admin.ModelAdmin):
    inlines = [
        CategoryInline,
    ]
admin.site.register(Post, PostAdmin)