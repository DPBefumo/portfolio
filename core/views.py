from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
def index(request):
    return render(request, 'core/index.html')


def project_detail(request):
    return render(request, 'core/projects.html')


def resume_detail(request):
    return render(request, 'core/resume.html')

def dog_adoption(request):
    return render(request, 'core/dog_adoption.html')
