from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required



@login_required(login_url="/login/")

# Create your views here.
def home(request):
    return render(request,'home.html')


# Create your views here.
def header(request):
    return render(request,'header.php')

# Create your views here.
def index(request):
    return render(request,'index.html')

@login_required(login_url="/login/")
def contact(request):
    return render(request,'contact.html')

def try1(request):
    return render(request,'try.html')

@login_required(login_url="/login/")
def Student_create(request):

    if request.method == "POST":
        data = request.POST

        name = data.get('name')
        photo = request.FILES.get('photo')
        contact_no = data.get('contact_no')
        dob = data.get('dob')
        resume = request.FILES.get('resume')
        skills = data.get('skills')

        Student.objects.create(
            name=name,
            photo=photo,
            contact_no = contact_no,
            dob = dob,
            resume =resume,
            skills=skills,
        )
        return redirect('/Student_create')

    queryset = Student.objects.all()
    context = {'Student_create':queryset}
    return render(request,'Student_create.html', context)



#
# def Student_create(request):
#     if request.method== 'POST':
#         e=stuform(request.POST)
#         if e.is_valid():
#             print('Form is valid')
#             try:
#                 e.save()
#                 return redirect('/Student_read/')
#              #   return HttpResponse('Form is submitted')
#              #   return redirect('/vegetable')
#             except:
#                 pass
#         else:
#             pass
#     else:
#         e=stuform()
#     return render(request,'Student_create.html',{'form':e})





def Student_read(request):
    e1=Student.objects.all()
    context={
        'e1':e1,
    }
    return render(request,'Student_read.html',context)


def Student_delete(request,id):
    e1=Student.objects.get(id=id)
    e1.delete()
    return redirect('/Student_create/')

#
# def Student_update(request,id):
#     e1=Student.objects.get(id=id)
#     if request.method == 'POST':
#         e = stuform(request.POST,instance=e1)
#         if e.is_valid():
#            # print('Form is valid')
#             try:
#                 e.save()
#                 return redirect('/Student_read/')
#             #   return HttpResponse('Form is submitted')
#             #   return redirect('/vegetable')
#             except:
#                 pass
#         else:
#             pass
#     else:
#         e = stuform()
#     return render(request,'Student_update.html',{'e1':e1,'e':e})


# def Student_update(request,id):
#     e1 = Student.objects.get(id=id)
#
#     if request.method == "POST":
#         data = request.POST
#
#         name = data.get('name')
#         photo = request.FILES.get('photo')
#         contact_no = data.get('contact_no')
#         dob = data.get('dob')
#         resume = request.FILES.get('resume')
#         skills = data.get('skills')
#
#         e1.name = name
#         e1.contact_no = contact_no
#         e1.skills = skills
#         if photo:
#             e1.photo = photo
#         if dob:
#             try:
#                 dob_date = datetime.strptime(dob, '%Y-%m-%d').date()
#                 e1.dob = dob_date
#             except ValueError:
#                 # Handle invalid date format
#                 pass
#         if resume:
#             e1.resume = resume
#
#         e1.save()
#         return redirect('/Student_create/')
#
#     context = {'student_instance': e1, 'student_data': e1.__dict__}
#
#     return render(request,'Student_update.html',context)


def Student_update(request, id):
    student_instance = Student.objects.get(id=id)

    if request.method == "POST":
        form = stuform(request.POST, request.FILES, instance=student_instance)
        if form.is_valid():
            form.save()
            return redirect('/Student_create/')
    else:
        form = stuform(instance=student_instance)

    context = {'form': form, 'student_instance': student_instance}

    return render(request, 'Student_update.html', context)


def login_page(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username = username).exists():
            messages.info(request, 'Invalid Username')
            return redirect('/login/')

        user = authenticate(username=username , password = password)

        if user is None:
            messages.error(request, 'Invalid Password')
            return redirect('/login/')
        else:
            login(request, user)
            return redirect('/Student_create/')

    return render(request, 'login.html')




def register_page(request):

    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username = username)

        if user.exists():
            messages.info(request, 'Username already taken')
            return redirect('/register/')

        user = User.objects.create(
            first_name = first_name,
            last_name=last_name,
            username = username
        )
        user.set_password(password)
        user.save()
        messages.info(request, 'account created successfully')
        return redirect('/register/')

    return render(request, 'register.html')


def logout_page(request):
    logout(request)
    return redirect('/login')
