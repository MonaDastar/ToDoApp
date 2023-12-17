import json

from django.shortcuts import  get_object_or_404,render
from django.http import HttpResponse, JsonResponse
from django.views import View

from task.models import User, Task


def index(request):
    return HttpResponse("welcome Mona")


def handle_error(message , status_code=400):
    return JsonResponse({
        "status" : "error",
        "message" : message
    }, status = status_code)
    

class UserAction(View):
    
    def post(self, request):
        if request.META.get('CONTENT_TYPE') != 'application/json':
            return handle_error("the content is not valid, must be json")
        data = json.loads(request.body)
        if "username" not in data:
            return handle_error("missed username field")
        else:
            user=User(username=data["username"])
            if "address" in data:
                user.address = data["address"]
            user.save()
            return JsonResponse({
                "status" : "success",
                "message" : f"user {user.username} with id of {user.id} created!"
            })



    
    def get(self, request):
        
        users=User.objects.all()
        result = []
        for user in users:
            result.append({
                "username":user.username,
                "address" : user.address,
                "user_id" : user.id,
                "createdAt" : user.createdAt
            })
        return JsonResponse(result, safe=False)



    def put(self,request, user_id):
        if request.META.get('CONTENT_TYPE') != 'application/json':
            return handle_error("the content is not valid, must be json")

        user = get_object_or_404(User, id= user_id)
        new_data = json.loads(request.body)
        if "username" in new_data:
            user.username = new_data["username"]
        if "address" in new_data :
            user.address = new_data["address"]
        user.save()
        return JsonResponse({
                "status" : "success",
                "message" : f"user {user.username}'s information updated!"
            })
        


    def delete(self,request, user_id):
        user = get_object_or_404(User, id=user_id)
        if request.method == "DELETE":
            user.delete()
            return JsonResponse({
                    "status" : "success",
                    "message" : f"user {user_id} deleted!"
                })

class TaskAction(View):
    
    def post(self,request,user_id):
        if request.META.get('CONTENT_TYPE') != 'application/json':
            return handle_error("the content is not valid, must be json")
        
        user = get_object_or_404(User, id= user_id)
        data = json.loads(request.body)
        if "title" not in data:
            return handle_error("missed title field")
        else:
            try:
                
                task=Task(title=data["title"], user=user)
                if "due_date" in data:
                    task.due_date = data["due_date"]
                task.save()
                return JsonResponse({
                    "status" : "success",
                    "message" : f"Dear {user.username} your task is {task.title}, good luck!"
                })
            except  Exception as e:
                # Handle IntegrityError and provide a meaningful response
                return handle_error(f"IntegrityError: {e}")

    def get(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        tasks = Task.objects.filter(user=user)
        result = []
        for task in tasks:
            result.append({
                "title": task.title,
                "task_id": task.id,
                "user_id": task.user.id,
                "done": task.done,
                "username": task.user.username,
                "createdAt": task.createdAt
            })
        return JsonResponse(result, safe=False)


    
    def put(self, request, user_id, task_id):  # Add 'self' as the first parameter
        if request.META.get('CONTENT_TYPE') != 'application/json':
            return handle_error("the content is not valid, must be json")
        
        user = get_object_or_404(User, id=user_id)  # Use 'self.get_object_or_404'
        task = get_object_or_404(Task, id=task_id, user=user)
        
        new_task = json.loads(request.body)
        for key, value in new_task.items():
            if key in ["title", "description", "due_date", "done"]:
                setattr(task, key, value)
        
        task.save()
        return JsonResponse({
            "title": "success",
            "message": f"{task.user}'s task updated!"
        })

        
        
    def delete(self,request, task_id):
        task = get_object_or_404(Task, id=task_id)
        if request.method == "DELETE":
            task.delete()
            return JsonResponse({
                    "status" : "success",
                    "message": f"Dear {task.user.username} you are dismissed from {task.title}, because the task is deleted!"
                })



    def get(self,request, user_id ):     
        user = get_object_or_404(User, id=user_id)
        tasks=Task.objects.filter(user=user)
        results = [
            {
                "title":task.title,
                "task_id":task.id,
                "user_id" : task.user.id,
                "username" : task.user.username,
                "createdAt" : task.createdAt
            }
                for task in tasks]
        return JsonResponse(results, safe=False)

        
        
    def get(self, request, user_id):  
        user = get_object_or_404(User, id=user_id)
        
        # Accessing query parameters
        title_query = request.GET.get('title', None)
        done_query = request.GET.get('done', None)

        # Filtering tasks based on query parameters
        tasks = Task.objects.filter(user=user)
        if title_query:
            tasks = tasks.filter(title__icontains=title_query)
        if done_query:
            tasks = tasks.filter(done=(done_query.lower() == 'true'))
        result = []
        for task in tasks:
            result.append({
                "title": task.title,
                "task_id": task.id,
                "user_id": task.user.id,
                "username": task.user.username,
                "createdAt": task.createdAt
            })
        return JsonResponse(result, safe=False)



