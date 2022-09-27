
from django.contrib import admin
from django.urls import path, include
from unity import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('unitymed.urls')),
    path('summernote/', include('django_summernote.urls')),
    path('editor/', include('django_summernote.urls')),
]  + static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
