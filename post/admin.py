from django.contrib import admin
from post.models import Category,Post,Tag,Contact


# Register your models here.

class CategorySlugAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

class PostSlugAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_filter =('status', 'tags')
    list_display = ('title','status','created_date','category','author')

class TagSlugAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Category, CategorySlugAdmin)
admin.site.register(Tag , TagSlugAdmin)
admin.site.register(Post,PostSlugAdmin)
admin.site.register(Contact)