from django.shortcuts import render,HttpResponse
from home.models import Contact

# Create your views here.
def index(request):
    context ={
        "name":"Lokesh Singh",
        "age":21
    }
    return render(request,"index.html",context)
    # return HttpResponse("this is home page")


def about(request):
    return HttpResponse("this is About page")

def services(request):
    return HttpResponse("this is Services page")

def contact_form(request):    
    # Get Method
    if(request.method =='POST'):
        name = request.POST['name']
        email = request.POST['email']
        ins = Contact(name=name,email=email)
        ins.save()
        print("The data is saved in database")
     
    return render(request,"contact.html")


# def form(request):
#     finalans = 0            
#     # Get Method
#     try:
     
#         n2 = request.GET['num1']
#         n1 = request.GET['num2']
#         finalans = int(n1)+int(n2)
#         print(n1)
#         print(n2)
#     except:
#         pass
#     return render(request,"form.html",{'output':finalans})



