from .views import make_menu
from django.urls import path

urlpatterns = [
    path('<str:name_menu>',make_menu, name="make_menu")
]
