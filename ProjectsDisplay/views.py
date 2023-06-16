from django.shortcuts import render
from ProjectsDisplay.models import Project

# Create your views here.
def ProjectsIndex(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'projects_display_index.html', context)

def ProjectDetail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'projects_display_detail.html', context)