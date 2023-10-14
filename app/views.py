from django.shortcuts import render,redirect
from app.models import slider,banner_area,MainCategory,Product



def base(request):
    return render(request,'base.html')

def singhup(request):
    return render(request,'singhup.html')

def index(request):
    sliders=slider.objects.all().order_by('-id')
    banner=banner_area.objects.all().order_by('-id')
    main_category=MainCategory.objects.all().order_by('-id')
    product=Product.objects.filter(section__name='Top Deal of the day')
    # print(product)

    context={
        'sliders':sliders,
        'banner':banner,
        'main_category':main_category,
        'product':product
    }
    # print(context)
    return render(request,'main/index.html',context)

def single_product(request,slug):
    return render(request,'product/product_detail.html')