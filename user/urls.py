from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from . import views
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from .forms import LoginForm

urlpatterns = [
   
    path('accounts/',include('django.contrib.auth.urls')),
    path("registration",views.CustomerRegistrationView,name="registration"),
    path("edit_profile",views.edit_profile,name="edit_profile"),
    path("add_adderss",views.add_adderss,name="add_adderss"),
    path("adderss",views.address,name='adderss'),
    path("dashbord",views.dashbord,name="dashbord"),
    path('accounts/login/',auth_views.LoginView.as_view(template_name='registration/login.html'))

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
