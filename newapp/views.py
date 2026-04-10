from django.shortcuts import render,redirect

# Create your views here.
from newapp.models import employee
from newapp.forms import emp_form

def emp(request):
    data=employee.objects.all()
    form=emp_form()
    if request.method=='POST':
        form=emp_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_page')
    context={'data':data,'form':form}
    return render(request,'empform.html',context)
        
            

def emp_delete(request,id):
    data=employee.objects.get(id=id)
    data.delete()
    return redirect("home_page")

