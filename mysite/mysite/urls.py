from argparse import Namespace
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

app__name = 'mysite'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myshop.urls', namespace='myshop')),
    path('', include('customers.urls', namespace='customers')),
    path('contact/', include('contact.urls', namespace='contact')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('',include('shop.urls',namespace='shop')),
    path('/checkout/',include('checkout.urls',namespace='checkout'))
]
# Static
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# Media
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)