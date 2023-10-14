from django.shortcuts import render,redirect
from app.models import slider,banner_area,MainCategory,Product
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages



def base(request):
    return render(request,'base.html')



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
    product=Product.objects.filter(slug=slug)
    if product.exists():
        product=Product.objects.get(slug=slug)
    else:
        return redirect ('404')

    context={
       'product':product, 
    }
    return render(request,'product/product_detail.html',context)
def Error404(request):
    return render(request,'errors/404.html')

def account(request):
    return render(request,'authentication/account.html')


def register(request):
    if request.method == "POST":
        username=request.POST.get('username')
        email=request.POST['email']
        password=request.POST['password']
        # print(username,email,password)
        user=User(
            username=username,
            email=email,
            password=password
        )
        user.set_password(password)
        user.save()

    return redirect('account')

def login_page(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            message=messages.error(request,'Email and Password are invalid')
            return redirect('account')

        
    return redirect('account')