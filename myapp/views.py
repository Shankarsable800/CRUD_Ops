from django.shortcuts import render,redirect
from myapp.form import *
from myapp.models import *
from django.urls import reverse
# Create your views here.

def home(request):
    response=render(request,"base.html",context={})
    return response

def addteacher(request):
    msg=' '
    if request.method=='POST':
        t=teacherform(request.POST)
        if t.is_valid():
            t.save()
            msg="teacher detailed added"
    form=teacherform()
    response=render(request,"addteacher.html",context={'form':form,'msg':msg})
    return response

def teacherlist(request):
    qs=teachers.objects.all()
    response=render(request,"teacherlist.html",context={"qs":qs})
    return response

def teacheredit(request,tname):
    t=teachers.objects.get(tname=tname)
    if request.method=="POST":
        form=teacherform(request.POST,instance=t)
        if form.is_valid():
            form.save()
            return redirect('teacherlist')
    else:
        form=teacherform(instance=t)
    return render(request,'editteacher.html',context={'form':form})

def teacherdelete(request,tname):
    qs=teachers.objects.filter(tname=tname)
    qs.delete()
    return redirect('teacherlist')

def studentadd(request):
    msg=""
    if request.method=='POST':
        form=studentform(request.POST)
        if form.is_valid():
            form.save()
            msg="Student detailed is saved"
        
    form=studentform()
    return render(request,"stu_add.html",context={'form':form,'msg':msg})

def studentlist(request):
    qs=students.objects.all()
    response=render(request,"stu_list.html",context={"qs":qs})
    return response

def studentdelete(request,Sname):
    qs=students.objects.filter(Sname=Sname)
    qs.delete()
    return redirect('studentlist')

def joinclassview(request):
    msg = ""
    qs1 = teachers.objects.all()
    qs2 = students.objects.all()

    if request.method == "POST":
        try:
            t = teachers.objects.get(tname=request.POST.get('teachers'))
            s = students.objects.get(Sname=request.POST.get('students'))
            courses = request.POST.get('courses')
            date = request.POST.get('date')
            slot = request.POST.get('slot')

            joinclass.objects.create(teachers=t, students=s, courses=courses, date=date, slot=slot)
            msg = "Class joined successfully!"
        except teachers.DoesNotExist:
            msg = "Teacher not found"
        except students.DoesNotExist:
            msg = "Student not found"

    return render(request, "joinclass.html", {'qs1': qs1, 'qs2': qs2, 'msg': msg})

def classlist(request):
    qs=joinclass.objects.all()
    res=render(request,"classlist.html",context={'qs':qs})
    return res


