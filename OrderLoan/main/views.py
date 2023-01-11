from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from .models import Loan_order
from .forms import OrderLoan
# Create your views here.

def index(response, id):
    cl = Loan_order.objects.get(id = id)
    orders = cl.orders_set.get()

    return HttpResponse("<h1>%s</h1><br> </br><p>%s</p>"%(cl.name, str(orders.amount)))

def home(response):
	return render(response, "main/home.html", {})


def added(response):
	return render(response, "main/added.html", {})


def loan(response):
    if response.method == "POST":
        form = OrderLoan(response.POST)

        if form.is_valid():
            
            fn = form.cleaned_data["Firstname"]
            Firstname = Loan_order(Firstname=fn)

            ln = form.cleaned_data["Lastname"]
            Lastname = Loan_order(Lastname=ln)

            lo = form.cleaned_data["Loan"]
            Loan = Loan_order(Firstname=lo)
            
            Firstname.save()
            Lastname.save()
            Loan.save()

        return render(response, "main/added.html", {})

    else:
        form = OrderLoan()
    form = OrderLoan()

    return render(response, "main/loan.html", {"form": form}) # goes inside views.py