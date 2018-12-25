from django.shortcuts import render,redirect,render_to_response
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.contrib import auth


from rest_framework import viewsets
from .serializers import ProjectSerializer

#own
from .models import (PLanguage,Project)
from contacts.models import Contact

def index(request):
    #TODO rest api
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

@login_required(login_url="../../accounts/register")
def detail(request,project_id):
    if request.method == 'POST':
        user = request.user
        project = Project.objects.get(pk=project_id)
        message = request.POST['message']
        c  = Contact.objects.get(project=project,user=user)
        if c:       
            contact = Contact(user=user,project=project,message=message)
            contact.save()
            #TODO send email to admin 
        else:
            messages.error(request,'Juz aplikowales')
            pass    
        return redirect('detail', project_id)

    else:
        project = Project.objects.get(pk=project_id)
        users = User.objects.filter(project=project)
        context = {
            'project':project,
            'users':users
        }

        return render(request, 'projects/detail.html',context)

@login_required(login_url="../../accounts/login")
def dashboard(request,project_id):

    user = request.user
    username = user.username

    project_author = Project.objects.filter(author=username)  
    project = Project.objects.get(pk=project_id)

    #get users which apply to this project
    request_users = Contact.objects.filter(project=project)

    if project in project_author:
       #auth user is author, can save it
       if request.method == 'POST':
          title = request.POST['title']
          desc  = request.POST['desc']
          github = request.POST['github']

          if title:
              project.title = title
          elif desc:
              project.desc = desc    
          elif github:
              project.github = github
          elif request.FILES['thumbnail']:
              thumbnail = request.FILES['thumbnail']
              fs = FileSystemStorage('media/images/projects')
              fs.save(thumbnail.name,thumbnail)
              project.thumbnail = 'images/projects/'+ thumbnail.name    
          project.save()

    else:
        return redirect('index')     

    context = {
        'project':project,
        'request_users': request_users,
    }   
    return render(request,'projects/dashboard.html',context)

@login_required(login_url="../../accounts/login")
def project_dashboard(request):
    user = request.user
    user_projects = Project.objects.filter(users=user)
    
    context = {
        'user_projects':user_projects
    }
    return render(request,'projects/pr_dash.html',context)

def add_user(request,project_id):
    user_id = request.POST['user_id']
    project = Project.objects.get(pk=project_id)
    if user_id:
        new_user = User.objects.get(pk=user_id)
        project.users.add(new_user)
        Contact.objects.get(project=project,user=new_user).delete()
    return redirect('dash',project_id)

def remove_user(request,project_id):
    user_id = request.POST['user_id']
    project = Project.objects.get(pk=project_id)
    if user_id:
        new_user = User.objects.get(pk=user_id)
        Contact.objects.get(project=project,user=new_user).delete()
        project.users.remove(new_user)
    return redirect('dash',project_id)

#api

class IndexApi(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
