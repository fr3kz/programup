from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.contrib import auth

#own
from .models import (PLanguage,Project)

def index(request):
    pinned_posts = Project.objects.filter(is_pinned=True)
    projects_python = Project.objects.filter(language__name='Python')
    projects_php = Project.objects.filter(language__name='Php')
    projects_cpp = Project.objects.filter(language__name='Cpp')
    finished_projects = Project.objects.filter(is_finished=True)
    unfinished_projects = Project.objects.filter(is_finished=False)

    context = {
        'pinned_projects':pinned_posts,
        'python':projects_python,
        'php':projects_php,
        'cpp':projects_cpp,
        'finished_projects':finished_projects,
        'unfinished_projects':unfinished_projects,
        }
    return render(request,"projects/index.html",context)

@login_required(login_url="../../accounts/register")
def create(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        description = request.POST['description']
        github = request.POST['github']
        title = request.POST['title']
        # GET AND SAVE PROJECT THUMBNAIL
        thumbnail = request.FILES['files']
        fs = FileSystemStorage('media/images/projects')
        fs.save(thumbnail.name,thumbnail)
        thumbnail_name = 'images/projects/' + thumbnail.name 
        
        #set current user as an author
        user = User.objects.get(id=user_id)
        user_name = user.username

        #create project
        pr = Project(thumbnail=thumbnail_name,author=user_name,description=description,github=github,title=title)
        pr.save()
        return redirect('index')
     
    return render(request,'projects/create.html')

def detail(request,project_id):
    #get particular project from given id
    project = Project.objects.get(pk=1)

    context = {
        'project':project,
    }

    return render(request, 'projects/detail.html',context)


# TODO: develop fninal function & this is working :O
def add_user(request,project_id):
    project = Project.objects.get(pk=1)
    if request.method == 'POST':
        usr = request.POST['user_id']
        userr = request.user
        
        project.users.add(userr)
        project.save()
        return redirect('index')