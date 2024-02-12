from django.shortcuts import render,redirect,get_list_or_404
from django.views import View
from home.models import Product
from .forms import CartAddForm
from .cart import Cart

# Create your views here.
class CartView(View):
    
    def get(self, request):
        cart = Cart(request)
        return render(request, 'orders/cart.html',{'cart':cart})
    
    

class CartAddView(View):
    def post(self, request,product_id):
        cart = Cart(request)
        product = get_list_or_404(Product, id = product_id)
        form = CartAddForm(request.POST)
        if form.is_valid():
           cart.add(product, form.cleaned_data['quantity'])
        return redirect('orders:cart')
    

class CartRemoveView(View):
    def get(self, request,product_id):
        cart = Cart(request)
        product = get_list_or_404(Product, id = product_id)
        cart.remove(product)
        return redirect('orders:cart')
