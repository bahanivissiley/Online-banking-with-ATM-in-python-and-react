"""
URL configuration for online_banking_and_atm project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from e_cash.views import ATMView, atm_withdrawal

urlpatterns = [
    path("admin/", admin.site.urls),
    path("atm/withdrawal/", atm_withdrawal, name="atm_withdrawal"),
    path("atm/", ATMView.as_view(), name="atm_list_create"),
    path("atm/<int:atm_id>/", ATMView.as_view(), name="atm_detail_update_delete"),
]
