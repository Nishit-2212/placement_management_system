from django.shortcuts import render
from .models import *

# Create your views here.
def Create_companies(request):

    if request.method == "POST":
        data = request.POST

        name = data.get('name')
        contact_no = data.get('contact_no')
        dob = data.get('dob')
        resume = request.FILES.get('resume')
        skills = data.get('skills')

        Company.objects.create(
            name=name,
            contact_no = contact_no,
            dob = dob,
            resume =resume,
            skills=skills,
        )

    return render(request,'Companies_create.html')