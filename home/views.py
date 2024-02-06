from django.shortcuts import render,get_object_or_404,redirect
from django.views import View
# Create your views here.
from .models import Product
from . import tasks
from django.contrib import messages
class HomeView(View):
    def get(self,reqest):
        products = Product.objects.filter(available=True)
        return render(reqest, 'home/home.html', {'products':products})
    


class ProductDetailView(View):
    def get(self,reqest,slug):
        product = get_object_or_404(Product, slug=slug)

        return render(reqest, 'home/detail.html', {'product':product})



class BucketHome(View):
    template_name = 'home/bucket.html'
    def get(self, request):
        objects = tasks.all_bucket_objects_task()
        # print('='*90)
        # print(objects)
        return render(request, self.template_name,{'objects':objects})


class DeleteBucketObject(View):
    def get(request,key):
        tasks.delete_object_task.delay(key)
        messages.success(request,'your object will be delete son','info')
        return redirect('home:bucket')