from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import get_user

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from notifications.signals import notify



@login_required
def accept_request(request, user_id):
    try:
        user_to_accept = User.objects.get(id=user_id)
    except User.DoesNotExist:
        messages.error(request, 'User does not exist')
        return redirect('/')

    # Assuming you have logic to determine the user who sent the request
    sender_user = request.user

    # Send a notification to the user who sent the request
    notify.send(
        sender=sender_user,
        recipient=user_to_accept,
        verb='accepted your request.',
    )

    # You can add your specific logic for accepting the request here

    messages.success(request, 'Request accepted successfully')
    return redirect('/')





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

def approve(request):
    return render(request,'approve.html')


@login_required(login_url="/login/")
def editprofile(request):
    if request.method == 'POST':
        # Handle form submission and update user's profile data here
        # You can access user data using request.user

        # Example:
        request.user.first_name = request.POST.get('first_name')
        request.user.last_name = request.POST.get('last_name')
        request.user.save()

        # Add more fields and save changes as needed
        current_password = request.POST.get('current_password')
        new_password = request.POST.get('new_password')
        confirm_new_password = request.POST.get('confirm_new_password')

        if current_password and new_password and confirm_new_password:
            # Check if the current password is correct
            if request.user.check_password(current_password):
                # Check if the new password and confirm password match
                if new_password == confirm_new_password:
                    # Set the new password and update the session auth hash
                    request.user.set_password(new_password)
                    update_session_auth_hash(request, request.user)  # Important for session security
                else:
                    messages.error(request, 'New passwords do not match.')
            else:
                messages.error(request, 'Current password is incorrect.')
        else:
            messages.error(request, 'Please fill in all password fields.')

        request.user.save()  # Save user profile changes

        messages.success(request, 'Profile updated successfully.')
        return redirect('/editprofile/')  # Redirect to the profile page or any other page



    return render(request,'editprofile.html')


@login_required(login_url="/login/")
def deleteprofile(request):
    if request.method == 'POST':
        # Handle form submission and delete the user's profile here
        user = request.user
        user.delete()
        messages.success(request, 'Your profile has been deleted.')
        return redirect('/login/')  # Redirect to the home page or any other page after deletion
    return render(request, 'deleteprofile.html')


@login_required(login_url="/login/")
def contact(request):
    return render(request,'contact.html')

@login_required(login_url="/login/")
def form(request):
    return render(request,'form.html')

def try1(request):
    return render(request,'try.html')

@login_required(login_url="/login/")
def Student_create(request):
    u = request.user.id
    print(u)

    if Student.objects.filter(user_id=u).exists():
        messages.error(request, "You have already submitted the form.")
        return redirect('/form')

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
            user_id=u
        )
        return redirect('/form')

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
            if username == "placement" and password == "123":
                # Assuming you don't have a User model entry for "placement"
                # This is a custom check for the specific username and password
                return redirect('/Student_create/')
            return redirect('/index/')

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
        return redirect('/login/')

    return render(request, 'register.html')


def logout_page(request):
    logout(request)
    return redirect('/login')


#
# def accept_form(request, form_id):
#     # Get the form instance
#     form_instance = Student.objects.get(pk=form_id)
#
#     # Update the form's acceptance status
#     form_instance.is_accepted = True
#     form_instance.save()
#
#     # Create a notification for the 1st user
#     Notification.objects.create(
#         user=form_instance.user,
#         message=f"Your form with ID {form_instance.id} has been accepted."
#     )
#
#     return JsonResponse({"message": "Form accepted successfully"})
#
# def reject_form(request, form_id):
#     # Get the form instance
#     form_instance = Student.objects.get(pk=form_id)
#
#     # Update the form's acceptance status
#     form_instance.is_accepted = False
#     form_instance.save()
#
#     # Create a notification for the 1st user
#     Notification.objects.create(
#         user=form_instance.user,
#         message=f"Your form with ID {form_instance.id} has been rejected."
#     )
#
#     return JsonResponse({"message": "Form rejected successfully"})
#
#
# def show_notifications(request):
#     # Get notifications for the current user
#     notifications = Notification.objects.filter(user=request.user).order_by('-created_at')
#
#     return render(request, 'notifications.html', {'notifications': notifications})