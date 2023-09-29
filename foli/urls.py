from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('projects/', views.allprojects, name="projects"),
    path('service/', views.service, name="service"),
    path('service-detail/<slug>', views.service_detail, name="service-detail"),
    path('project/<slug>', views.project_detail, name="project"),
]
urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_URL)