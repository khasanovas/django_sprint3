from django.contrib import admin

from .models import Category, Location, Post


# class BlogAdmin(admin.ModelAdmin):


admin.site.register(Category)
admin.site.register(Location)
admin.site.register(Post)
