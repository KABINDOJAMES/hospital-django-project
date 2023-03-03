from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Service, Contact, Pharmacy, SocialMediaLinks, AboutUs, Home
from django.contrib import messages
from django.db.models import Q

# Create your views here.
def index(request):
    services = Service.objects.all()
    media_links = SocialMediaLinks.objects.all()
    home = Home.objects.filter()[:1].get()
    return render(request, 'unitymed/index.html', {'services':services, 'media_links':media_links, 'home':home})

def contact(request):
    services = Service.objects.all()
    media_links = SocialMediaLinks.objects.all()
    return render(request, 'unitymed/contact.html', {'services':services, 'media_links':media_links})


def about(request):
    services = Service.objects.all()
    media_links = SocialMediaLinks.objects.all()
    aboutus = AboutUs.objects.filter()[:1].get()
    return render(request, 'unitymed/about.html', {'services':services, 'media_links':media_links, 'aboutus':aboutus})

def pharmacy(request):
    services = Service.objects.all()
    pharmacy = Pharmacy.objects.filter()[:1].get()
    media_links = SocialMediaLinks.objects.all()
    return render(request, 'unitymed/pharmacy.html', {'services':services, 'pharmacy':pharmacy, 'media_links':media_links})

def services(request):
    services = Service.objects.all()
    media_links = SocialMediaLinks.objects.all()
    return render(request, 'unitymed/services.html', {'services':services, 'media_links':media_links})

def search(request):
    query = request.GET.get('q', '')
    search_results = Service.objects.filter(Q(title__icontains=query) | Q(description__icontains=query)) 
    services = Service.objects.all()
    media_links = SocialMediaLinks.objects.all()
    return render(request, 'unitymed/search.html', {'services':services, 'search_results':search_results, 'query':query, 'media_links':media_links})


def service_detail(request, slug):
    service_item = Service.objects.get(slug=slug)
    services = Service.objects.all()
    media_links = SocialMediaLinks.objects.all()
    return render(request, 'unitymed/service-detail.html', {'service_item':service_item, 'services':services, 'media_links':media_links})

def contact(request):
    services = Service.objects.all()
    media_links = SocialMediaLinks.objects.all()
    if request.method == 'POST':
        post_data = request.POST.copy()
        email = post_data.get("email", None)
        name = post_data.get("name", None)
        subject = request.POST.get("subject", None)
        message = request.POST.get("message", None)
        contact = Contact()
        contact.email = email
        contact.name = name
        contact.subject = subject
        contact.message = message
        
        # save in model
        contact.save()
        messages.success(request, 'Your request has been received. We will get back to you shortly')

        #res = JsonResponse({'msg': 'Your request has been received'})
        #return res
        return redirect('index')
       
    return render(request, 'unitymed/contact.html', {'services':services, 'media_links':media_links})