from django.contrib import admin
from task.models import Task, User

admin.site.register(User)
admin.site.register(Task)

#cusomize the table by modelAdmin