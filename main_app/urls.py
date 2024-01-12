#  all paths specific to catcollector

from django.urls import path
# eventually will be pointing to view functionality which handles our Req & Res
from . import views
# from views import CatList

# step 1 -> in main/urls.pydefine the path
# step 2 -> create anticipates views function ->
    # view.home -> we anticipate there to be a home function within views.py
# step 3 -> create anticipated html file in template file



urlpatterns =[
    # RESTful Path
    path('',views.home, name='home'),
    # \ comes wiith " "8000 no need to add for next pages
    path('about/', views.about, name='about'),
    
    path('cats/', views.cats_index, name='index'),
    path('cats/<int:cat_id>/', views.cats_detail, name='detail'),

    # as_view() is a method inherited from ListView to CatList -> returns views.CatList -> which is defind as class in views
        # as_view() method turns the class to a function -> since path wants a fn for its second argument
    # CBV automatically render a template following teh cinvention ->
        # templates/cat(modelname)_list.html
    # path('cats/', views.CatList.as_view(), name='cats_list'), 

    path('cats/create/', views.CatCreate.as_view() ,name ='cat_create'),
    path('cats/<int:pk>/update/', views.CatUpdate.as_view() ,name ='cat_update'),
    path('cats/<int:pk>/delete/', views.CatDelete.as_view() ,name ='cat_delete'),

    path('cats/<int:cat_id>/add_feeding/', views.add_feeding, name = 'add_feeding'),

]


'''
Creating Data Using a CBV - C in CRUD :

Step 1 - Identify the Route
If this was an Express app, we likely would need to code two separate routes and controller actions like:

router.get('/cats/new', catsCtrl.new); to view the form, and
router.post('/cats', catsCtrl.create); to add the cat to the database and then redirect

However, using Django, we only need a single URL-based route because a CreateView CBV will automatically:

    Create a Django  MODELFORM used to automatically create the form's inputs for the Model.
    Handle the Request:
    Display -> GET request ===> Render and display a template (html). On that template, well include a <form>, it will display our Form.
    Creat -> POST request ===> Use the posted forms contents to (automatically and transparently) create data and perform a redirect (usually to our index page)
'''

