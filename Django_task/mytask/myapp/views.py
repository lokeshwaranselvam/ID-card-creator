from django.shortcuts import render
from .models import Student

# Create your views here.


def home(request):

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        age = request.POST.get("age")

        Student.objects.create(
            name=name,
            email=email,
            age=age
        )

    students = Student.objects.all()

    return render(request,"form.html",{"students":students})   