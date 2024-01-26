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

    path('spots', views.index, name='index'),
    path('spots/<int:sighting_id>', views.spot, name='spot'),
    path('spots/recent', views.recent, name='recent'),
    path('spots/<int:breed_id>', views.by_breed, name='breed'),
    path('spots/<int:city_id>', views.by_city, name='city'),
    path('spots/<int:user_id>', views.user_spots, name='user'),

    #path('spots/search', views.spot_search, name='search'),
    path('spots/<int:sighting_id>', views.update_spot, name='spot_upd'),
    path('spots/<int:sighting_id>', views.delete_spot, name='spot_del'),

    path('spots/compose', views.post_sighting, name='spot_new')
]
