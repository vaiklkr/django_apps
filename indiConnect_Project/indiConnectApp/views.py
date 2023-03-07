from django.shortcuts import render
from .models import users
def input(request):
    return render(request, 'base1.html')

def insert(request):
    if request.method == 'POST':
        user_obj = users.objects.all()  #if u want display all objects
        user_t = request.POST.get('user_txt')
        pass_t = request.POST.get('pass_txt')
        #import pymysql
        #con = pymysql.connect()
        user_data = users(user_name=user_t, pass_word=pass_t)
        user_data.save()
    return render(request, 'base2.html')