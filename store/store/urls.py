from django.contrib import admin
from django.urls import path
from . import views
from .controllers.authorization import api_register, api_login
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
<<<<<<< Updated upstream
    path('cart/', views.cart_view, name='cart'),

=======

    #API
    path('api/register', api_register, name='api_register'),
    path('api/login', api_login, name='api_login'),
>>>>>>> Stashed changes
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
