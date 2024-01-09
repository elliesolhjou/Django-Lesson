from django.shortcuts import render

# Create your views here.
# request passed to here
# it retruns a reesponse, render 

# step 1 -> in main/urls.pydefine the path
# step 2 -> create anticipates views function ->
    # view.home -> we anticipate there to be a home function within views.py
# step 3 -> create anticipated html file in template file


# home view
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')