from django.contrib import admin

# Register your models here.
from .models import Department,Employee,Salary,Leave,Job


admin.site.register(Employee)
admin.site.register(Department)
admin.site.register(Leave)
admin.site.register(Salary)
admin.site.register(Job)