from django.shortcuts import render

# Create your views here.

def input(request):
    return render(request, 'base1.html')

def display(request):
    prodid = request.GET["txt1"]
    prodname = request.GET["txt2"]
    price = float(request.GET["txt3"])
    qty = int(request.GET["txt4"])
    dict1 = {"prod_id": prodid, "prod_name": prodname, "prod_price": price, "prod_qty": qty}
    return render(request, 'base2.html', context=dict1)
