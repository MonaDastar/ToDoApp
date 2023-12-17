from django.contrib import admin
from django.urls import path, include
from task.views import index, UserAction,TaskAction

urlpatterns = [
    path("", index),
    path("users/", UserAction.as_view()),
    path("user-list/", UserAction.as_view()),
    path("update-user/<int:user_id>/", UserAction.as_view()),
    path("delete-user/<int:user_id>/", UserAction.as_view()),
    path("create-task/<int:user_id>/", TaskAction.as_view()),
    path("list-task/<int:user_id>/", TaskAction.as_view()),
    path("update-task/<int:user_id>/<int:task_id>/", TaskAction.as_view()),
    path("delete-task/<int:task_id>/", TaskAction.as_view()),
    path("search-task-by-userid/<int:user_id>/", TaskAction.as_view()),
    path("search-task/<int:user_id>/", TaskAction.as_view()),   
]
