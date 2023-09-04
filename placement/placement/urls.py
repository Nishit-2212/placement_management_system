"""
URL configuration for placement project.

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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from user.views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = ([
    path('admin/', admin.site.urls),
    path('students/', include('user.urls')),
    path('Student_create/', Student_create),
    path('Student_read/',Student_read),
    path('Student_delete/<int:id>/',Student_delete),
    path('Student_update/<int:id>/',Student_update),
    path('login/',login_page),
    path('register/',register_page),
    path('logout/',logout_page),
    path('header/',header),
    path('index/',index),
    path('contact/', contact),
    path('editprofile/',editprofile),
    path('deleteprofile/',deleteprofile),
    path('try/',try1),

    # path('user/', Create_student),
    # path('home/', home),


]
+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT))
#
# if settings.DEBUG:
#     urlpattern= += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT))
#
# urlpattern += staticfiles_urlpatterns()
