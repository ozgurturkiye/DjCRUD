"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("coreapp.urls")),
    path("f1/", include("f1.urls")),
    path("f2/", include("f2.urls")),
    path("f3/", include("f3.urls")),
    path("c1/", include("c1.urls")),
    path("c2/", include("c2.urls")),
    path("c3/", include("c3.urls")),
    path("apis/1.0/", include("apis1.urls")),
    path("apis/2.0/", include("apis2.urls")),
    path("apis/3.0/", include("apis3.urls")),
]
