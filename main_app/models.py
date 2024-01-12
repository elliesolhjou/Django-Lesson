# from unittest.util import _MAX_LENGTH
from django.db import models
from django.urls import reverse

MEALS =(
('B', 'Breakfast'), 
('L', 'Lunch'), 
('D', 'Dinner')
)

# Create your models here.
class Cat(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()

    def __str__(self):
        return f'Hi my name is {self.name}'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'cat_id': self.id})
        # it makes url route for new added data to DB and create a detail page for them with this id
    #  and takes you to the detail page of new data - > creates url for new model instance
    

class Feeding(models.Model):
    date = models.DateField('Feeding Date')
    meal = models.CharField(
    max_length=1,
    # add the 'choices' field option
    choices=MEALS,
    # set the default value for meal to be 'B'
    default=MEALS[0][0]
  )
    # Create a cat_id FK -> this is how associations forms
    # the One side gets referred in many side as FK
      # Create a cat_id FK
    # ForeignKey -> cretaed OnetoMany relationship
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE, null= True)
    # since feeding belongs to a cat it should hold cats ID -> FK

    def __str__(self):
        # Nice method for obtaining the friendly value of a Field.choice(MEAL)
        return f'{self.get_meal_display()} on {self.date}'
    
    
    class Meta:
        ordering=['-date']