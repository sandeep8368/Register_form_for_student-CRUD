from django.shortcuts import render
from django.http import HttpResponse
from home.models import Register

# Create your views here.
def index(request):
    return render(request,'Register.html')
def submit_form(request):
    if request.method =='POST':
        First_Name = request.POST['First_Name']
        Last_Name = request.POST['Last_Name']
        Email_id = request.POST['Email_id']
        Password = request.POST['Password']
        Phone_No = request.POST['Phone_No']
        Gender = request.POST['Gender']
        Area_Python = request.POST.get('Python','off')
        Area_C = request.POST.get('C Lang','off')
        Area_Node = request.POST.get('Node js','off')
        Area_Java = request.POST.get('Java','off')
        Area_Mern = request.POST.get('Mern','off')
        AOI = []
        if Area_Python =="Python":
            AOI.append(Area_Python)
        if Area_C == "C Lang":
             AOI.append(Area_C)
        if Area_Node == "Node js":
             AOI.append(Area_Node)
        if Area_Java == "Java":
             AOI.append(Area_Java)
        if Area_Mern == "Mern":
             AOI.append(Area_Mern)
             
        print(First_Name,Last_Name,Email_id,Password,Phone_No,Gender,*AOI)
        Register(First_Name = First_Name,Last_Name = Last_Name,Email_id =Email_id,Password = Password,Phone_No = Phone_No,Gender= Gender,Area_of_Interest = AOI).save()
        msg="Form Submitted Successfully"
        return render(request,'Register.html',{'msg':msg})
        
        
        
        
    else:
        return HttpResponse("<h1>404 not found</h1>")