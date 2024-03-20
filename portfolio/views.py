from django.shortcuts import render
from .models import Project
# Create your views here.

def home(request):
    projects = Project.objects.all() # saare projects objects of a project like title, description, image ko fetch kar liya
    return render(request,'portfolio/home.html', {'projects' : projects})# ek dictionary banai jismein projects will be key and projects(fetched) will be value
# request keyword super duper important
