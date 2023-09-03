from django.shortcuts import render

# import forms for form
from .forms import Table1

# import model (database) 
from .models import Table1_models
# Create your views here.


def home(requests):

    #create object of form, which will use to print form on template.
    f = Table1()

    print(requests.user)
    # object of model, here it is useful to print all existing data to the template.  
    t = Table1_models.objects.filter(user_name = requests.user)


    # Let's print above object on terminal. 
    # for i in (list(t)):
    #     print(i.name, i.email, i.desc)

    # print(type(t))

    # Check if request is post or not.
    if requests.method == "POST":

        # Models object which will  use to save data to the database. 
        m1 = Table1_models()

        # get data from request. 
        name = requests.POST["name"]
        email = requests.POST["email"]
        desc = requests.POST["desc"]
        userid = requests.POST["iduser"]

        # display data to the terminal. 
        # print(name, email, desc)

        # Save fatched data to the database. 
        m1 = Table1_models(name = name, email = email, desc = desc, user_name = userid)
        print(userid)
        # finally store data to the database. 
        m1.save()

    return render(requests, "index.html", {"tb": f, "tabledisp": t})
