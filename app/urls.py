from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('base',views.base,name='base'),
    path('',views.index,name='index'),
    path('singhup',views.singhup,name='singhup'),
    path('product/<slug:slug>',views.single_product,name='product_detail')
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
