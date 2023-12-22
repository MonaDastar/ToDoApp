from django.contrib import admin
from django.urls import path, include
from task.views import index, UserListView,CreateUserView, UserDetailView, TaskListView, TaskDetailView
#TODO change urls to user or users, action or actions
urlpatterns = [
    path("", index, name="index"),
    path("users/", UserListView.as_view(),  name="user_list"),
    path("create-user/", CreateUserView.as_view(), name="create_user"),

    path("users/<int:user_id>/", UserDetailView.as_view()),
    path("task/<int:user_id>/", TaskListView.as_view()),
    path("update-task/<int:user_id>/<int:task_id>/", TaskDetailView.as_view()),
    path("delete-task/<int:task_id>/", TaskDetailView.as_view()),
]
