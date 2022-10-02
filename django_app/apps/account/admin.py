from django.contrib import admin

from .models import Departament, Location, Profile, Wallet, Achievement, Position


class LocationTabInlines(admin.TabularInline):
    model = Location
    extra = 1


@admin.register(Departament)
class DepartamentAdmin(admin.ModelAdmin):
    pass


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    inlines = [LocationTabInlines, ]


@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    pass


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    pass


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    pass
