from django.shortcuts import render,get_object_or_404,redirect
from django.views import View
# Create your views here.
from .models import Product,Category
from . import tasks
from django.contrib import messages
from utils import isAdminUserMixin
from orders.forms import CartAddForm
class HomeView(View):
    def get(self,reqest,category_slug=None):
        products = Product.objects.filter(available=True)
        categories = Category.objects.filter(is_sub = False)
        if category_slug :
            category = Category.objects.get(slug = category_slug)
            products = products.filter(category=category)
        return render(reqest, 'home/home.html', {'products':products,'categories':categories})
    


class ProductDetailView(View):
    def get(self,reqest,slug):
        product = get_object_or_404(Product, slug=slug)
        form = CartAddForm()
        return render(reqest, 'home/detail.html', {'product':product, 'form':form})



class BucketHome(isAdminUserMixin,View):
    template_name = 'home/bucket.html'
    def get(self, request):
        objects = tasks.all_bucket_objects_task()
        # print('='*90)
        # print(objects)
        return render(request, self.template_name,{'objects':objects})
    


class DeleteBucketObject(isAdminUserMixin,View):
    def get(self,request,key):
        tasks.delete_object_task.delay(key)
        messages.success(request,'your object will be delete son','info')
        return redirect('home:bucket')

class DownloadBucketObject(isAdminUserMixin,View):
    def get(self,request,key):
        tasks.download_object_task.delay(key)
        messages.success(request,'your download  will be start soon','info')
        return redirect('home:bucket')
  