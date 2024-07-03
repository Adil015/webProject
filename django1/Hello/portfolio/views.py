from django.shortcuts import render, HttpResponse
from datetime import datetime
from portfolio.models import Contact 
from portfolio.models import Intro
from portfolio.models import Edu 
from portfolio.models import Project
from portfolio.models import Skill
from portfolio.models import Exp
 
# Create your views here.
def index(request):
    introdata = Intro.objects.first()
    edu = Edu.objects.all()
    projects = Project.objects.all()
    sk = Skill.objects.all()
    exp = Exp.objects.all()
    return render(request, 'index.html',{'introdata': introdata, 'edu': edu, 'projects': projects, 'sk': sk, 'exp':exp})

def contact(request):
    if request.method == 'POST':
        comment = request.POST.get('comment')
        email = request.POST.get('email')
        contact = Contact(comment=comment, email=email)
        contact.save()
    return render(request, 'index.html')

