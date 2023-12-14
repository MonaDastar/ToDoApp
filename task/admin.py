from django.contrib import admin
from task.models import Task, User

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'address', 'createdAt', 'updatedAt')
    search_fields = ('username', 'address')
    list_filter = ('createdAt', 'updatedAt')

class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'due_date', 'done', 'user', 'createdAt', 'updatedAt')
    search_fields = ('title', 'description', 'user__username')
    list_filter = ('due_date', 'done', 'createdAt', 'updatedAt')

admin.site.register(User, UserAdmin)
admin.site.register(Task, TaskAdmin)

