from django.shortcuts import render,redirect
from app.models import slider



def base(request):
    return render(request,'base.html')

def index(request):
    sliders=slider.objects.all()
    context={
        'sliders':sliders
    }
    print(context)
    return render(request,'main/index.html',context)

# Create your views here.
