from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('base',views.base,name='base'),
    path('',views.index,name='index'),
    path('product/<slug:slug>',views.single_product,name='product_detail'),
    path('404',views.Error404,name='404'),
    # authentication
    path('account/register',views.account,name='account'),
    path('register/acount',views.register,name='register'),
    path('account/login',views.login_page,name='login')


]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
