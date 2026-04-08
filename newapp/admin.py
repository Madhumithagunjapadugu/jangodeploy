from django.contrib import admin

# Register your models here.
from newapp.models import employee
class emp_admin(admin.ModelAdmin):
    list_display=['emp_id','emp_name','emp_salary','emp_dept']
admin.site.register(employee,emp_admin)