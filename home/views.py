from django.shortcuts import render
from django.views import View
# Create your views here.


class HomeView(View):
    def get(self,reqest):
        return render(reqest, 'home/home.html')

