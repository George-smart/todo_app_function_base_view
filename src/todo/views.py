from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from .models import TodoApp
from .form import TodoForm


# Create your views here.
@login_required(login_url='signin')
def index(request):
    if request.method == "POST":
        form_class = TodoForm(request.POST)
        if form_class.is_valid():
            todoApp = form_class.save(commit=False)
            todoApp.user = request.user
            todoApp.save()
            
            return redirect('/')
    else:
        form_class = TodoForm()   
    
    todos = TodoApp.objects.filter(user=request.user)

    return render(request, 'index.html', {'form_class': form_class, 'todos': todos})


def complete(request, pk=None):
    todoApp = TodoApp.objects.get(id=pk)
    if todoApp.is_complete == True:
        todoApp.is_complete = False
    else:
        todoApp.is_complete = True
    todoApp.save()
    return redirect('home')        


@login_required(login_url='signin')
def editTodo(request, pk):
    todos = get_object_or_404(TodoApp, pk=pk)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todos)
        if form.is_valid():
            todos = form.save(commit=False)
            todos.user = request.user
            todos.save()
            return redirect('home')
    else: 
        form = TodoForm(instance=todos) 
    return render(request, 'update.html', {'form': form})


def deleteTodo(request, pk=None):
    todo = TodoApp.objects.get(id=pk)
    todo.delete()
    return redirect('/')

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email already exist")
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, "Username Already Exist")
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()     
                
                return redirect('signin')       
        else:
            messages.info(request, "Password didn't matched")
            return redirect('signup')

    return render(request, 'signup.html')


def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, "Invalid Credentials")
            return redirect('signin')
         
    return render(request, 'signin.html')


def signout(request):
    auth.logout(request)
    return redirect('signin')