from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate
from .models import tbl_Authentication,tbl_Companydetails
from .forms import Companymaster
from django.shortcuts import render, redirect ,get_object_or_404 
from django.contrib import messages 
 
def CreatecompanyNew(request):
    ddlcompanyobjects= tbl_Companydetails.ddlcompanyobjects.all()
 
    if request.method == 'POST':
        form = Companymaster(request.POST)
        print(form.errors,form)
        if form.is_valid(): 
            user = form.save(commit=False)                
            user.save()                
            return render(request,'company.html',{'form':form,'ddlcompanyobjects':ddlcompanyobjects})
    else:
        form = Companymaster()
    return render(request,'company.html',{'form':form,'ddlcompanyobjects':ddlcompanyobjects})
def Editcompany(request, id):      
    ddlcompanyobjects = tbl_Companydetails.ddlcompanyobjects.get(id=id)      
    return render(request,'EditCompany.html', {'ddlcompanyobjects':ddlcompanyobjects})  
 
  
def Updatecompany(request, id):
        print('t')          
        obj= get_object_or_404(tbl_Companydetails, id=id)       
        form = Companymaster(request.POST, instance= obj)
        context= {'form': form}
        print(obj)
        if form.is_valid():
            ddlcompanyobjects = tbl_Companydetails.ddlcompanyobjects.all()               
            user = form.save(commit=False)      
            user.save()       
            messages.success(request, "You successfully updated the Data")
            context= {'form': form}                           
            return render(request, 'company.html',{'form':form,'ddlcompanyobjects':ddlcompanyobjects})
        else:
            context= {'form': form,
                           'error': 'The Data  was not updated successfully.'}
            return render(request,'company.html' , context)
def Deletecompany(request, id): 
    ddlcompanyobjects = tbl_Companydetails.ddlcompanyobjects.get(id=id)       
    ddlcompanyobjects.delete()
    return redirect('/CreatecompanyNew')