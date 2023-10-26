from django.db import models
from Django import forms 
 
class tbl_Companydetails(models.Model):
 
    companyName =  models.CharField(max_length = 150)
    Address = models.CharField(max_length = 500)
    contactNo = models.CharField(max_length=15)
    establisheddate = models.DateField(null=True, blank=True)
    websitelink = models.CharField(max_length=50,default='')
    emailaddress = models.CharField(max_length=50,default='')   
  
 
    def __str__(self):
        return self.companyName
    ddlcompanyobjects = models. Manager()
