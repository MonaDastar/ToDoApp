from django.test import TestCase
from django.utils import timezone
from task.models import User, Task



class UserModelTest(TestCase):
    def test_create_user(self):
        # Get the initial user count
        user_count = User.objects.count()
        
        #create a user
        user = User.objects.create(username="test_user", address="Test Address")
        
        #check if the user is created successfully 
        self.assertEqual(User.objects.count(),user_count+1)
        self.assertEqual(user.username,"test_user" )
        self.assertEqual(user.address,"Test Address" )
    
    def test_update_user(self):
        user = User.objects.create(username="testuser2", address="Test Address2")
        
        user.address = "Update Address"
        user.save()
        
        updated_user = User.objects.get(id=user.id)
        self.assertEqual(updated_user.address, "Update Address")
        
        
    def test_delete_user(self):
        user_count = User.objects.count()
        user = User.objects.create(username="testuser3",address="Test Address")
        user.save()
        user.delete()
        self.assertEqual(User.objects.count(),user_count)
        
class TaskModelTest(TestCase):
    
    def setUp(self):
        self.user = User.objects.create(username="testuser2", address="Test Address2")

    
    def test_create_task(self):
        
        task = Task.objects.create(title="clean the house", user=self.user)
        task_user_title = Task.objects.get(title="clean the house",user=self.user)
        self.assertEqual(task_user_title,task)
        
    def test_update_task(self):
        task = Task.objects.create(title="test task", user=self.user)
        
        task.title = "updated_title"
        task.save()
        
        updated_task = Task.objects.get(id=task.id)
    
        self.assertEqual(updated_task.title,"updated_title")
        
    def test_delete_task(self):
        
        task = Task.objects.create(title="test task", user=self.user)
        
        task_count=Task.objects.count()
        
        task.delete()
        
        self.assertEqual(Task.objects.count(), task_count-1)
        
    
