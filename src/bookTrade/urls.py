"""bookTrade URL Configuration

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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.conf import settings
from reviews.views import review_view, maps_view, maps_detail_view
from payments.views import signup_view, login_view, profile_view, logout_view, create_image, book_detail, find_book

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reviews/', review_view ),
    path('search/', maps_view),
    path('results/', maps_detail_view),
    path('payments/signup',signup_view),
    path('payments/login',login_view),
    path('payments/profile',profile_view),
    path('payments/logout',logout_view),
    path('payments/bookupload', create_image),
    path('payments/viewbooks', book_detail),
    path('payments/finduser', find_book)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)