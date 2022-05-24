from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def detail(request,pk):
    photo_selected=photo.objects.get(id=pk)


    return render(request,'photos/detail.html',{'photo':photo_selected})

def add(request):
    categories=category.objects.all()

    if request.method=="POST":
        data=request.POST
        image = request.FILES.get("images")

        if data['category']!="none":
            cat=category.objects.get(id=data['category'])
        elif data['category_new']!="":
            cat, created=category.objects.get_or_create(category_name=data['category_new'])
        else:
            cat=None

        pho=photo.objects.create(
            description=data['description'],
            category_name=cat,
            image=image
            
        )
        return redirect('home')
    return render(request,'photos/add.html',{'categories':categories})

def home(request):
    if request.method=="GET":
        cate=request.GET.get('category')
        

        if cate==None:
            photos=photo.objects.all()
        else:
            cats=category.objects.filter(category_name=cate)
            cat=cats.first()
            photos=photo.objects.filter(category_name=cat)

            #photos=photo.objects.filter(category_name__category_name==cate)
    else:
        photos=photo.objects.all()

        

    #photos=photo.objects.all()
    categories=category.objects.all()
    context={'photos':photos,'categories':categories}
    return render(request,'photos/home.html',context)