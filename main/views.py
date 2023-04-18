from django.shortcuts import render, redirect
from main.models import Company
from .models import Employee
import json

# Create your views here.


def companies_view(request):
    
    companies = Company.objects.values_list('name', flat=True)
    employees = Employee.objects.all().values('first_name', 'last_name', 'company')
    employees_list = list(employees)
    employees_json = json.dumps(employees_list)
    
    return render(request, 'companies.html', {'companies':companies, 'empjson':employees_json})



def employee_dropdown(request):

    if request.method == 'POST':
        user_input = request.POST.get('employee')
        tag = request.GET.get('tag')

        record_to_update = Employee.objects.get(id=user_input)
        record_to_update.company = tag
        record_to_update.save()

        return redirect('/') 

    employees = Employee.objects.all()
    return render(request, 'employee_dropdown.html', {'employees': employees})

