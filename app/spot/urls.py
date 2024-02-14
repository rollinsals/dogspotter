"""spot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from spotapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),

    path('spots', views.IndexView.as_view(), name='index'),
    path('spots/<int:pk>/', views.SpotView.as_view(), name='detail'),

    path('api/spots', views.index, name='index'),
    path('api/spots/<int:sighting_id>', views.spot, name='spot'),
    path('api/spots/recent', views.recent, name='recent'),
    path('api/spots/breed/<slug:breed>', views.by_breed, name='breed'),
    path('api/spots/city/<slug:city>', views.by_city, name='city'),
    path('api/spots/<slug:user>', views.user_spots, name='user'),

    #path('spots/search', views.spot_search, name='search'),
    path('api/spots/<int:sighting_id>', views.update_spot, name='spot_upd'),
    path('api/spots/<int:sighting_id>', views.delete_spot, name='spot_del'),

    path('api/spots/compose', views.post_sighting, name='spot_new')
]
