from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    
    path('', views.test, name="test"),
    path('product/<int:pk>', views.product, name="product"),
    path('base/', views.base, name="base"),path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('tracker/', views.tracker, name='trackingstatus'),
    path('search/', views.search, name='search'),
    path('checkout/', views.checkout, name='checkout'),
    # path('test1/', views.test1, name="test1")
]
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)