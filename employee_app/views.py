from django.shortcuts import render, redirect
from django.views import View
from .models import Employee
from django.http import HttpResponseRedirect
from django.urls import reverse

class MainPageView(View):

    def get(self, request):
        employees_obj = Employee.objects.all()
        total_employee = Employee.objects.all().count()
        return render(request, 'index.html', context={
            'employees' : employees_obj,
            'total_employee' : total_employee
        })

    def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        employee = Employee(name=name, email=email, address=address, phone=phone)
        employee.save()
        url = reverse("main-page")
        return HttpResponseRedirect(url)


class DeleteEmployeeView(View):
    def post(self, request, id):
        employee_obj = Employee.objects.get(id=id)
        employee_obj.delete()
        url = reverse("main-page")
        return HttpResponseRedirect(url)

