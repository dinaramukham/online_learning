from django.contrib import admin

from .models import User, Payment


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone', 'city', 'avatar')
    list_filter = ('email', 'phone', 'city', 'avatar')
    search_fields = ('email', 'phone', 'city', 'avatar')


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('user', 'courses', 'lesson', 'method_pay', 'date_payment', 'money')
    list_filter = ('user', 'courses', 'lesson', 'method_pay', 'date_payment', 'money')
    search_fields = ('user', 'courses', 'lesson', 'method_pay', 'date_payment', 'money')