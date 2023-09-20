from django.shortcuts import render, HttpResponse, redirect
from home.models import Contact
from django.contrib.auth import authenticate


# Create your views here.
def index(request):
    context = {"name": "Lokesh Singh", "age": 21}
    return render(request, "index.html", context)
    # return HttpResponse("this is home page")


def about(request):
    # return HttpResponse("this is About page")
    return render(request, "about.html")


def service(request):
    # return HttpResponse("this is Services page")
    return render(request, "service.html")


# Create database in django and save data in database(C)
def contact(request):
    # post Method
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        password = request.POST["password"]
        ins = Contact(name=name, email=email, password=password)
        ins.save()
        print("The data is saved in Contact database")

    return render(request, "contact.html")


# Fetch data from database(R)
def getdata(request):
    data = Contact.objects.all()

    # Method - 1
    # data1 = Contact.objects.filter(name="Lokesh Singh", password="1234")

    # Method- 2
    data1 = Contact.objects.all().filter(name="Lokesh Singh", password="1234")
    return render(request, "get_data.html", {"data": data, "data1": data1})


# Update data in database(U)
def update(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        old_password = request.POST["old_password"]
        new_password = request.POST["new_password"]
        Contact.objects.filter(name=name, email=email, password=old_password).update(
            password=new_password
        )
        print("The data is updated in Contact database")
    return render(request, "update_data.html")


# Delete data from database(D)
def delete(request):
    if request.method == "POST":
        name = request.POST["name"]
        password = request.POST["password"]
        Contact.objects.filter(name=name, password=password).delete()
        print("The data is deleted from Contact database")
    return render(request, "delete.html")


# def login(request):
#     if(request.method=="POST"):
#         username = request.POST['username']
#         password = request.POST['password']


#         user = authenticate(username = username,password = password)

#         if(user is not None):
#             login(request,user)
#             return redirect('next')


#     return render(request,"login.html")

# def next(request):
#     return render(request,"next.html")


# # Get Method
# if request.method == "GET":
#         name = request.GET["name"]
#         email = request.GET["email"]
#         password = request.GET["password"]
