from django.contrib import admin

# Register your models here.
from .models import Member,Role,Fees_plan

admin.site.register(Member)
admin.site.register(Role)
admin.site.register(Fees_plan)