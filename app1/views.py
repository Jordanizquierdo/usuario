from django.shortcuts import render,redirect
from app1.models import User
from app1.forms import FormUser
# Create your views here.

def index(request):
    return render(request,'app1/index.html')


def listaUsers(request):
    usuarios = User.objects.all()
    data = {'usuarios':usuarios}
    return render(request,'app1/usuarios.html',data)


def agregarUser(request):
    form = FormUser()
    if request.method == 'POST':
        form = FormUser(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/usuarios')
    data = {'form':form}
    return render(request,'app1/agregarUsuario.html',data)



def actualizarUser(request,id):
    user = User.objects.get(id=id)
    form = FormUser(instance=user)
    if request.method=='POST':
        form = FormUser(request.POST,instance=user)
        if form.is_valid():
            form.save()
        redirect('/usuarios')
    data = {'form':form}
    return render(request,'app1/agregarUsuario.html',data)

def eliminarUser(request,id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect('/usuarios')