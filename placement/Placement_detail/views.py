from django.shortcuts import render
from .models import *
from user.models import Student


# Create your views here.



def home(request):
    student_data = Student.objects.all()  # You can add filtering if needed

    # Pass the data to the template context
    context = {'students': student_data}
    return render(request, 'placement-portal.html', context)
