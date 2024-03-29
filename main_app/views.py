from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView,UpdateView, DeleteView
from .models import Cat
from .forms import FeedingForm

# Create your views here.
# request passed to here
# it retruns a reesponse, render 

# step 1 -> in main/urls.pydefine the path
# step 2 -> create anticipates views function ->
    # view.home -> we anticipate there to be a home function within views.py
# step 3 -> create anticipated html file in template file
# cats = [
#   {'name': 'Lolo', 'breed': 'tabby', 'description': 'furry little demon', 'age': 3},
#   {'name': 'Sachi', 'breed': 'calico', 'description': 'gentle and loving', 'age': 2},
# ]

# home view
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def cats_index(request):
  # We pass data to a template very much like we did in Express!
  cats = Cat.objects.all()
  return render(request, 'cats/index.html', {
    'cats': cats,
  })

def cats_detail(request, cat_id):
  #  Cat is a class -> needs instanciation
   cat=Cat.objects.get(id=cat_id)
  #  FeedingForm is a class -> needs instanciation
   feeding_form = FeedingForm()
  #  we needd to pass along the form to show up on detail page -> we pass it to html 
  #  as an object to be rendered on html
  #  no need to create table on detail page
   return render(request, 'cats/detail.html', {'cat': cat, 'feeding_form': feeding_form
  })

'''
# List View is built-in CBV functionality for index/showall
# CatList is inheriting index functionality from ListView -> inheriting methods etc
# model = cat -> asks CatList to retrieve database objects by using Cat Model
class CatList(ListView):
   model = Cat
  # we can set the template_name attribute to render a template other than the default
    # instead of having def cat_index(request): 
                              # return render (request, 'cat/index.html) -> we can use template_name = X
   template_name = 'cat/index.html' #-> render index.html located in cat dir
'''


# by convention CatCreate CBV -> looks for template/main_app/cat_form.html
class CatCreate(CreateView):
# The fields attribute is required for a CreateView
  model = Cat
  fields='__all__'
  # alternative: fields = ['name', 'breed', 'description', 'age']
  #  success url handles redriecting
  # success_url = '/cats/{cat_id}' # <--- must specify an exact ID
  # Or..more fitting... you want to just redirect to the index page
  # success_url = '/cats'
  # cat id is not defined for CBV -> get_absolute_url method in Model


class CatUpdate(UpdateView):
  model = Cat
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['breed', 'description', 'age']


class CatDelete(DeleteView):
  model = Cat
  success_url = '/cats'

# CBV IS BEST PRACTICE TO CRUD
  # CBV automatically created nstance for ModelForm
  # CBV under the hood grabs the input inside instance of ModelForm and pass it to server
  # CBV automatically save() after any CRUD


# manual way of form and input generation
  # STEP1 - TOUCH FORMS.PY with Meta class
def add_feeding(request, cat_id):
   # create a ModelForm instance using the data in request.POST
  feeding_form = FeedingForm(request.POST)
  print('hitting here 0')
  # validate the form
  if feeding_form.is_valid():
    print (True)
    # don't save the form to the db until it
    # has the cat_id assigned
    new_feeding = feeding_form.save(commit=False)
    new_feeding.cat_id = cat_id
    print('hitting here')
    new_feeding.save()
    print('hitting here2')
  return redirect('detail', cat_id=cat_id)



'''
ListView enables you to create CBV which comes with benefits

BENEFITS OF USING CBV AND IMPORTED LISTVIEW: --> LISTVIEW GIVES YOU FULL CRUD options

- ListView -> INDEX OR LISTING ALL IN DB --> is the same as cat_index
- DetailView - used to implement the “detail” page for an object --> is the same as cat_detail
- CreateView - used to create an object
- DeleteView - used to delete an object
- UpdateView - used to update an object

'''

# Why We are USing CBV -> DRY to avoid CRUD application pattern repitiotions

'''
 We didn't have to put that route above the 'cats/<int:cat_id>/' because, 
 unlike with Express, Django won't match that route unless there's something 
 that looks like an integer in the second segment, thus it ignores cats/create/
 '''