from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myshop.urls', namespace='myshop')),
    path('', include('customers.urls', namespace='customers')),
    path('', include('contact.urls', namespace='contact')),
    path('blog', include('blog.urls', namespace='blog')),
]
# Static
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# Media
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)