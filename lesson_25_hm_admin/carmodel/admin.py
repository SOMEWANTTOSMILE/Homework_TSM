from django.contrib import admin
from .models import Car, CarModel, User, Brand


class CarModelInline(admin.TabularInline):
    model = CarModel


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    ordering = ('name',)
    inlines = [CarModelInline]


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("car_model", 'vin', 'is_active')
    search_fields = ('vin', )


@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    ordering = ('name',)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    search_fields = ('phone_number', )
