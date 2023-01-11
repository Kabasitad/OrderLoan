from django import forms

class OrderLoan(forms.Form):
    Firstname = forms.CharField(label = "Firstname",max_length=200)
    Lastname = forms.CharField(label = "Lastname",max_length=200)
    Loan = forms.IntegerField(label = "Loan Amount")