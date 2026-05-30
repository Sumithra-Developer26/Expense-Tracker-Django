from django.shortcuts import render, redirect
from .models import Expense

def expense_home(request):
    expenses = Expense.objects.all()

    if request.method == "POST":
        title = request.POST['title']
        amount = request.POST['amount']
        category = request.POST['category']

        Expense.objects.create(
            title=title,
            amount=amount,
            category=category
        )
        return redirect('/')

    return render(request, 'expense.html', {'expenses': expenses})