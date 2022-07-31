from unicodedata import name
from django.shortcuts import render
import random

# Create your views here.

# Home page
def home(request):
    return render(request,'authentication/home.html')


# about page 
def generate_password(request):

    # extract request data 

    length = int(request.GET.get('password_length', '15'))

    # generated password
    newly_generated_password = ""

    # characters

    chars = 'abcdefghijklmnopqrstuvwxyz'


    if request.GET.get('uppercase') :
        chars = chars + 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    
    if request.GET.get('numbers') :
        chars = chars + '1234567890'


    if request.GET.get('special_chars') :
        chars = chars + '*/-_=+*&^%$#@!~'


    chars = list(chars)


    for iterator in range(length):
        newly_generated_password += random.choice(chars)

    # pass data to template 
    return render(request,'authentication/generated_password.html',{ 'generated_password': newly_generated_password})


def about(request):
    return render(request, 'authentication/about.html')