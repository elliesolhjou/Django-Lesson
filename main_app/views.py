from django.shortcuts import render
from .models import Cat

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
   cat=Cat.objects.get(id=cat_id)
   return render(request, 'cats/detail.html', {'cat':cat})