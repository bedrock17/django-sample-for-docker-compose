from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.

from django.http import HttpResponse

from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

from .models import Board
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'index.html')

@login_required
def edit(request, id):
    data = get_object_or_404(Board, pk=id)
    if data == None:
        return redirect("/")

    if data.user != request.user:
        return redirect("/")

    if request.method == "GET":
        context = {"data": data}
        return render(request, 'edit.html', context)
    else:
        data.title = request.POST["title"]
        data.content = request.POST["content"]

        data.save()
        return redirect("/list")

@login_required
def write(request):
    if request.method == "GET":
        return render(request, 'write.html')
    else:
        try:
            title = request.POST["title"]
            content = request.POST["content"]
            b = Board(title=title, content=content, user=request.user)
            
            b.save()
            return redirect("/list")

        except Exception as e:
            return HttpResponse("ERROR " + str(e))

@login_required
def delete(request, id):
    data = get_object_or_404(Board, pk=id)

    if data != None:
        if data.user == request.user:
            data.delete()

    return redirect("/list")

@login_required
def read(request, id):
    data = get_object_or_404(Board, pk=id)

    if data == None:
        return redirect("/list")
        
    deletable = data.user == request.user
    
    context = {"data": data, "deletable": deletable}
    return render(request, "read.html", context)

def userLogin(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        id = request.POST["id"]
        password = request.POST["password"]

        user = authenticate(request, username=id, password=password)

        if user == None:
            return redirect("/login")
        else:
            login(request, user)
            return redirect("/")

@login_required
def userLogout(request):
    logout(request)
    return redirect("/")

@login_required
def list(request):
    boardList = Board.objects.filter(user=request.user)
    context = {"BoardList": boardList, "Length": len(boardList)}
    return render(request, 'list.html', context)

@login_required
def listAll(request):
    boardList = Board.objects.all()
    context = {"BoardList": boardList, "Length": len(boardList)}
    return render(request, 'list.html', context)

def signup(request):
    if request.method == "GET":
        return render(request, "signup.html")
    else:
        id = request.POST["id"]
        password = request.POST["password"]

        print("=====[%s]==[%s:%s]", request.method, id, password)
        
        try:
            user = User.objects.create_user(username=id, password=password)
            user.save()
            login(request, user)
            return redirect("/")

        except Exception as e:
            error_msg = {"msg": 'Username is already taken. Please choose a different Username.'}
            return render(request, "signup.html", error_msg)

    error_msg = {"msg": '????'}
    return render(request, "signup.html", error_msg)

