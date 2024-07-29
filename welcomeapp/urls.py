from django.urls import path
from . import views
from .views import SIView,Calc
urlpatterns=[
    path('',views.index,name='index'),
    path('swap',views.swap,name='swap'),
    path('si',SIView.as_view()),
    path('calc',Calc.as_view())
]