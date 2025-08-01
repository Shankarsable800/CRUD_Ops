from django.contrib import admin
from myapp.models import teachers, students, joinclass

admin.site.register(teachers)
admin.site.register(students)
admin.site.register(joinclass)