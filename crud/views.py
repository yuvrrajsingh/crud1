from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .forms import StudentRegistration
from .models import User

# Create your views here.

def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            f = StudentRegistration()
            mydict = {'form': f}
            '''
            # Another way to save data
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=pw)
            reg.save()
            '''

            fm.save()
            return redirect('/')

    elif request.method == 'GET':
        fm = StudentRegistration()
        mydict = {
            'form': fm,
            'stud': User.objects.all()
        }
        return render(request, 'crud/addandshow.html', context=mydict)

def edit(request, i):
    y = User.objects.get(id=i)
    if request.method == 'POST':
        f = StudentRegistration(request.POST, instance=y)
        if f.is_valid():
            f.save()

        return redirect('/')


    else:
        f = StudentRegistration(instance=y)

        return render(request, 'crud/updatestud.html', {'form':f, 'id':i})





def delete(request, i):
    y = User.objects.get(id=i)
    y.delete()
    return redirect('/')