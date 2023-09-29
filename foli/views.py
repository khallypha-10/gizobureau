from django.shortcuts import render, redirect
from . models import Contact, Member, Project, Service
from django.contrib import messages
from django.core.paginator import Paginator
# Create your views here.


def navba(request):
    projectss = Project.objects.all().last()
    proje = Project.objects.all()[:2]
    context = {"proje": proje, "projectss":projectss}
    return render(request, "navbar.html", context)


def home(request):
    projects = Project.objects.all()[:5]
    services = Service.objects.all()
    members = Member.objects.all()
    project = Project.objects.all().count()
    context = {"projects":projects, "services": services, "members": members, "project": project}
    return render(request, "home.html", context)


def about(request):
    return render(request, "about.html")

def contact(request):
    if request.method == 'POST':
        first_name = request.POST['name']
        last_name = request.POST['lastname']
        phone = request.POST['phone']
        email = request.POST['email']
        message = request.POST['message']
        contact = Contact(first_name=first_name, last_name=last_name, phone=phone, email=email, message=message)
        contact.save()
        messages.success(request, 'Your message was received. We will get back to you shortly')
        return redirect("home")
    return render(request, "contact.html") 

def allprojects(request):
    p = Paginator(Project.objects.all(), 5)
    page = request.GET.get('page')
    projects = p.get_page(page)
    context = {"projects":projects}
    return render(request, "projects.html", context)

def project_detail(request, slug):
    project = Project.objects.get(slug=slug)
    projects = Project.objects.all()[:4]
    context = {"project": project, "projects": projects}
    return render(request, "project-detail.html", context)

def service(request):
    services = Service.objects.all()
    context = {"services": services}
    return render(request, "service.html", context)

def service_detail(request, slug):
    service = Service.objects.get(slug=slug)
    context = {"service": service}
    return render(request, "service-details.html", context)