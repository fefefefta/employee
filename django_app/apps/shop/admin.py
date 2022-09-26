from django.contrib import admin

from .models import Tag, Category, Product, Image, Comment


class ImageTabInlines(admin.TabularInline):
    model = Image
    extra = 1


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageTabInlines, ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
