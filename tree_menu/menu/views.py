from django.shortcuts import render
from .models import Menu

def make_menu(request,name_menu):
    items = Menu.objects.filter(name = name_menu).select_related('parent')
    return render(request, 'menu/menu.html',{'items': items})
