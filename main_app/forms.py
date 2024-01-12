from django.db.models.base import Model
from django.forms import ModelForm
from .models import Feeding

# manual way of creating forms - instead of CBV
class FeedingForm(ModelForm):
  class Meta:
    # NESTED META CLASS:
        # Tells Django it shoudl be connected to Model Feeding
        # Tells Django to which fields of the Feeding model should be included in the form.
        # CBV does everything for us underthehood -> but if you want to do it manuallyy you have to use nested META class
    model = Feeding
    fields = ['date', 'meal']


'''
Note that our custom form inherits from ModelForm and has a nested class Meta: 
to declare the Model being used and the fields we want inputs generated for

'''

# We have generated a form and integrated it to a model -. BUT IT IS A CLASS
# -> it needs to be instanciated -> otherwise it doesnt work -> WHERE?
    # WHERE DOES IT TO BE INSTANCIATED?
        # WHERE WE WANT TO PERFORM OPERATIONS ON IT - we want it inside cat detail page to add food ->
            # what hits tha path for details page to render the add feerinf form? 
            # views.cat_detail function
                # ||
                # ||
                # ||
                # \/
                # VIEWS.PY -> to instanciate the form 