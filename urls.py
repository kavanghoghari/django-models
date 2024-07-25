"""kavanf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core.views import index
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from core import views
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

app_name = "urls"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  # Home page
    path('products/', views.product_list, name='product_list'),  # Product list page
    path('category/', views.category_list_view, name='category-list'),  # Category list page

    path('user/', category_list_views , include("userauths.urls")),  # User authentication URLs
]
from django.contrib import admin



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('sim.urls')),

   
]
#python manage.py tailwind start use everytime 
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # Other paths...
]