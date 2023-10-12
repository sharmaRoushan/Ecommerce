from django.contrib import admin
from .models import*
class Product_images(admin.TabularInline):
    model=Product_image
class Additional_infomations(admin.TabularInline):
    model=Additional_infomation

class Product_admin(admin.ModelAdmin):
    inlines=(Product_images,Additional_infomations)
    list_display=('product_name','price','category','section')
    list_editable=('category','section')
admin.site.register(slider)
admin.site.register(banner_area)
admin.site.register(MainCategory)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Section)
admin.site.register(Product,Product_admin)
admin.site.register(Product_image)
admin.site.register(Additional_infomation)




# Register your models here.
