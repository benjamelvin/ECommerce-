from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import csv
from .csv_dictreader import CSV_Interface
from django.views.decorators.csrf import csrf_exempt
import requests 
from requests_oauthlib import OAuth1
import pprint
from dotenv import load_dotenv
import os

load_dotenv()


products_interface = CSV_Interface('./store_app/data/products.csv')
shopping_cart_interface = CSV_Interface('./store_app/data/shopping_cart.csv')
# Create your views here.
def index(request):
   data = products_interface.no_copies()
   catagories = {'products': data}     
   # print(data)
  
   return render(request, 'index.html', catagories)


def catagory(request, name):
   
   data = []
   for i in products_interface.all_data:
     
      if i['category'] == name:
         data.append(i)
  
   return render(request, 'catagory.html', {'data':data})

def product(request, id):
   data ={}
   holder=[]
   print(id)
   for i in products_interface.all_data:
      
      if i['id'] == str(id):
         holder.append(i)
   data = {'products':holder}
   print(data)
   return render(request, 'product.html', data)


def add_product(request):
    
   value=request.POST.get('model')
   shopping_cart_interface.append_one_row_to_file({'id': value,'quantity': 1})
   return HttpResponseRedirect('/')

def shopping(request):
   shopping_cart_interface.update_data_from_file()
   holder = []
   total = 0
   for i in shopping_cart_interface.all_data:
      id=i['id']
      
      for j in products_interface.all_data:
         if j['id'] == id:
            total+= float(j['cost'])
            holder.append({'product': j['name'],'cost': j['cost'],'quantity': i['quantity']})
   data = products_interface.unique_counter(holder)
   data.append({'total':round(total,2)})
   return render(request, 'shopping-cart.html', {'products': data})
def search1(request):
   return render(request, 'search.html')


def search(request, name):
   
   

   auth = OAuth1(os.environ['apikey'], os.environ['secretkey'])
   endpoint = f"http://api.thenounproject.com/icon/{name}"
   response = requests.get(endpoint, auth=auth)
   response_json = response.json()
   

   # pp.pprint(response_json['icon'])
   
   return JsonResponse(response_json)