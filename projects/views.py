from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
import datetime
#own
from .models import Project
from .forms import CreateProjectForm

# TODO create index function for main page & display pinned projects and categories
# TODO create view for particular project & view for your project (details etc.)
def index(request):
    return

@login_required
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
        
        #get current user as an author
        user = User.objects.get(id=user_id)
        user_name = user.username

        #create project
        pr = Project(thumbnail=thumbnail_name,author=user_name,description=description,github=github,title=title)
        pr.save()
        return redirect('index')
     
    return render(request,'projects/create.html')

def detail(request):
    return