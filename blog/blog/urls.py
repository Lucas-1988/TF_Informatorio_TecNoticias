from django.contrib import admin
from django.urls import path, include
from apps.posts.views import posts
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views




urlpatterns = [
    path('admin/', admin.site.urls), #!SACAR ADMIN
    path('', include('apps.posts.urls')), 
    path ('', posts, name='posts'),
    path('', views.index, name='index'),
    path('contacto/', views.contacto, name='contacto'),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




