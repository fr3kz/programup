from django.shortcuts import render,redirect,render_to_response
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
from django.contrib import auth


#own
from .models import (PLanguage,Project)
from contacts.models import Contact

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
    
    if request.method == 'POST':
        user = request.user
        project = Project.objects.get(pk=project_id)
        message = request.POST['message']
        contact = Contact(user=user,project=project,message=message)
        contact.save()
        return redirect('detail', project_id)

    else:
        project = Project.objects.get(pk=project_id)
        users = User.objects.filter(project=project)
        context = {
            'project':project,
            'users':users
        }

        return render(request, 'projects/detail.html',context)
#TODO:DASHBOARD
def dashboard(request):
    return