from django.urls import path
from . import views
 
urlpatterns = [
    path("",views.base,name="base"),
  
 
    path('CreatecompanyNew/',views.CreatecompanyNew,name='CreatecompanyNew'),
    path('Editcompany/<int:id>', views.Editcompany,name="Editcompany"),
    path('Updatecompany/<int:id>', views.Updatecompany,name="Updatecompany"), 
    path('Deletecompany/<int:id>', views.Deletecompany,name="Deletecompany"), 
     
]