from django.urls import path
from . import views
from unity import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('pharmacy/', views.pharmacy, name='pharmacy'),
    path('service-detail/<slug:slug>/', views.service_detail, name='service-detail'),
    path('services/', views.services, name='services'),
    
]  + static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

