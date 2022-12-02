from django.shortcuts import render
from django.http.response import HttpResponse
from . import views
# Create your views here.
all_dummy_foods = [
  {
    'id':1,
    'title':'Dark Choco Premium',
    'price':499,
    'is_premium':True,
  },
  {
    'id':2,
    'title':'Red Spicy',
    'price':349,
    'is_premium':False,
  },
  {
    'id':3,
    'title':'Blue Glacier',
    'price':349,
    'is_premium':False,
  },
]
def foods(request):
    context = {'foods':all_dummy_foods}
    return render(request,"app_foods/foods.html",context=context)

def food(request,food_id):
    instand_food = None
    #context = set
    try:
      instand_food = [f for f in all_dummy_foods if f['id'] == food_id][0]
    except IndexError:
      print("except : Not Data")
    context = {'food':instand_food}
    return render(request,"app_foods/food.html",context=context)

# https://www.youtube.com/watch?v=BBL8W-lpNHw&t=2745s 2.00.00
