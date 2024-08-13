from django.shortcuts import render
import datetime
from .models import Test_list
from .models import Todo_list

# Create your views here.
def home (request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        date = request.POST['date']
#calling our model
        task = Test_list()
        task.name = name
        task.email = email
        task.message = message
        task.date = date 
        task.save()

    task_list = Test_list.objects.all()#using this model go fetch objects and return them here.
    context ={
        'tasks': task_list
    }

    return render(request,"home.html", context)

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if username == 'Afrah' and password == 'apple':
            return render(request,"home.html")
    

    return render(request,"login.html")


def register(request):
    return render(request,"register.html")

def calculator(request):
    if request.method == 'POST':
        num1 = request.POST['num1']
        num2 = request.POST['num2']
        print(num1,num2)
        total = int(num1) + int(num2)

        context ={
            'total': total
        }
        return render(request,"calculator_result.html",context)
    else:
        return render(request,"calculator.html")
    

"""def todo(request):
        if request.method =='POST':
             print('Do something here')
             title = request.
        return render(request,"todo.html")"""

def contact(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        last_name = request.POST['last name']
        email = request.POST['email']
        phone_number = request.POST['phone number']
        
    return render(request,"contact.html")



def todo (request):
    if request.method == 'POST':
        title = request.POST['title']
        date = request.POST['date']
        description = request.POST['description']
        label = request.POST['label']
#calling our model
        task = Todo_list()
        task.title = title
        task.date = date
        task.description = description
        task.label = label 
        task.save()

    task_list = Todo_list.objects.all()#using this model go fetch objects and return them here.
    context ={
        'tasks': task_list
    }

    return render(request,"todo.html", context)


def index(request):
    return render(request,"index.html")