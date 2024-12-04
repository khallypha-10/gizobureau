from django.shortcuts import render, redirect
from . models import Contact, Project, Service
from django.contrib import messages
from django.core.paginator import Paginator
from django.core.mail import send_mail, BadHeaderError
# Create your views here.



def home(request):
    projects = Project.objects.all()[:15]
    services = Service.objects.all()
    project = Project.objects.all().count()
    context = {"projects":projects, "services": services, "project": project}
    return render(request, "home.html", context)


def about(request):
    return render(request, "about.html")

def contact(request):
    if request.method == 'POST':
        first_name = request.POST['name']
        last_name = request.POST['lastname']
        phone = request.POST['phone']
        email = request.POST['email']
        budget = request.POST['budget']
        currency = request.POST['currency']
        message = request.POST['message']
        contact = Contact(first_name=first_name, last_name=last_name, phone=phone, email=email, message=message)
        contact.save()
        
        subject = "Inquiry" 
        body = {
		    'first_name': first_name, 
			'last_name': last_name, 
            'phone': phone,
			'email': email, 
            'currency': currency, 
            'budget': budget,
			'message':message, 
            }
        message = "\n".join(body.values()) 

        try:
            send_mail(subject, message, 'gizobureau@gmail.com', ['gizobureau@gmail.com']) 
        except BadHeaderError: #add this
                return HttpResponse('Invalid header found.')
        
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