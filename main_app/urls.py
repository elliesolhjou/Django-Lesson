#  all paths specific to catcollector

from django.urls import path
# eventually will be pointing to view functionality which handles our Req & Res
from . import views

# step 1 -> in main/urls.pydefine the path
# step 2 -> create anticipates views function ->
    # view.home -> we anticipate there to be a home function within views.py
# step 3 -> create anticipated html file in template file



urlpatterns =[
    path('',views.home, name='home'),
    # \ comes wiith " "8000 no need to add for next pages
    path('about/', views.about, name='about'),
    
    path('cats/', views.cats_index, name='index'),
]