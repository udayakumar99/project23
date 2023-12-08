from django.contrib import admin

# Register your models here.

from app.models import *
admin.site.register(department)

admin.site.register(employee)

admin.site.register(salgrade)

admin.site.register(bonus)