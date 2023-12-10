from django.urls import path
from task.views import index, CreateUser, ListUser, UpdateUser, DeleteUser, CreateTask,  ListTask, UpdateTask, DeleteTask, SearchTaskByUserId, SearchTask


urlpatterns = [
    path("",index),
    path("users/", CreateUser.as_view()),
    path("user-list/", ListUser.as_view()),
    path("update-user/<int:user_id>/", UpdateUser.as_view()),
    path("delete-user/<int:user_id>/", DeleteUser.as_view()),
    path("create-task/<int:user_id>/",CreateTask.as_view() ),
    path("task-list/", ListTask.as_view()),
    path("update-task/<int:task_id>/",UpdateTask.as_view()),
    path("delete-task/<int:task_id>/",DeleteTask.as_view()),
    path("search-task-by-userid/<int:user_id>/",SearchTaskByUserId.as_view()),
    path("search-task/<int:user_id>/", SearchTask.as_view()),    
    
]
