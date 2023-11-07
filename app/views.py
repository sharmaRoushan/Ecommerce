from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from app.models import slider,banner_area,MainCategory,Product,Category
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.template.loader import render_to_string
from django.http import JsonResponse


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

@login_required(login_url='login')
def register(request):
    if request.method == "POST":
        username=request.POST.get('username')
        email=request.POST['email']
        password=request.POST['password']
        # print(username,email,password)
        if User.objects.filter(username=username).exists():
            message=messages.error(request,'username is already exists')
            return redirect('login')
        if User.objects.filter(email=email).exists():
            message=messages.error(request,'email is already exists')
            return redirect('login')
        user=User(
            username=username,
            email=email,
        )
        user.set_password(password)
        user.save()
    return redirect('login')
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
            return redirect('login')   
    return redirect('login')
@login_required(login_url='/accounts/login')
def profile_logout(request):
    return render(request,'profile/profile.html')

@login_required(login_url='/accounts/login')
def update_profile(request):
    if request.method == "POST":
        username=request.POST.get('username')
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        password=request.POST.get('password')
        user_id=request.user.id
        user=User.objects.get(id=user_id)
        user.first_name=first_name
        user.last_name=last_name
        user.email=email
        user.username=username
        if password!=None and password !="":
            user.set_password(password)
        user.save()
        message=messages.success(request,'Profile are update successfully')
    return redirect('profile')
def Logout(request):
    logout(request)
    return redirect('index')
def aboutus(request):
    return render(request,'main/about.html')
def contact(request):
    return render(request,'main/contact.html')
def all_product(request):
    category=Category.objects.all()
    product=Product.objects.all()
    context={
        'category':category,
        'product':product,
    }
    return render(request,'product/product.html',context)
def filter_data(request):
    categories=request.GET.getlist('category[]')
    brands=request.GET.getlist('brand[]')
    allProducts=Product.objects.all().order_by('-id').distinct()
    # print(allProducts)
    if len(categories)>0:
        allProducts=allProducts.filter(category_id__in=categories).distinct()
    if len(brands)>0:
        allProducts=allProducts.filter(Brand__id_in=brands).distinct()
    t=render_to_string('ajax/product.html',{'product':allProducts})
    return JsonResponse({'data':t})