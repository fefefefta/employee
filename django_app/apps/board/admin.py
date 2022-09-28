from django.contrib import admin

from .models import Payment, Idea, Location, Event, Image


class PaymentTabInlines(admin.TabularInline):
    model = Payment
    extra = 1


class LocationTabInlines(admin.TabularInline):
    model = Location
    extra = 1


class ImageTabInlines(admin.TabularInline):
    model = Image
    extra = 1


@admin.register(Idea)
class IdeaAdmin(admin.ModelAdmin):
    inlines = [PaymentTabInlines, ]


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    inlines = [LocationTabInlines, ImageTabInlines]


