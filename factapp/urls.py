from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('table',views.table,name='table'),
    path('squarecube',views.squarecube,name='squarecube'),
    path('calc',views.calc,name='calc'),
    path('message',views.message,name='message'),
    path('radioexample',views.radioexample,name='radioexample'),
    path('checkboxexample',views.checkboxexample,name='checkboxexample'),
     path('dropdownlistexample',views.dropdownlistexample,name='dropdownlistexample')
]