from django.contrib import admin
from django.contrib.auth.models import Group,User
from .models import PaymentDetail

# Register your models here.

admin.site.unregister(Group)
admin.site.unregister(User)

@admin.register(PaymentDetail)
class PaymentAdmin(admin.ModelAdmin):
	list_display=[field.name for field in PaymentDetail._meta.get_fields()]
	exclude=['addedBy',]
	list_filter=['member']
