from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect
from django.urls import reverse
from app.models import JobPost

job_title = [
    "First Job",
    "Second Job",
    "Third Job",
]

job_description = [
    "First Job Description",
    "Second Job Description",
    "Third Job Description",
]

# Create your views here.
class TempClass:
    x = 5


def hello(request):
    list = ["alpha","beta"]
    temp = TempClass()
    is_authenticated = True
    context={"name":"Django", "age":10, "first_list":list, "temp_object": temp, "is_authenticated": is_authenticated}
    return render(request, "app/hello.html", context)


def job_list(request):
    jobs = JobPost.objects.all()
    context={"jobs":jobs}
    return render(request, "app/job_list.html", context)

def job_detail(request,id):
    try:
        if id == 0:
            return redirect(reverse('jobs_home'))
        job = JobPost.objects.get(id=id)
        context = {"job":job}
        return render(request, "app/job_detail.html", context)
    except:
        return HttpResponseNotFound("Not Found")