from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDolist,Item
from .forms import CreateNewList

# Create your views here.
def home (response):
    l = ToDolist.objects.all()
    return render(response, "main/home.html", {"l":l})
   #return HttpResponse("<h1> HI SI ACHREF !! </h1>")

def create (response):
    l = ToDolist.objects.all()
    if response.method == "POST" :
        form = CreateNewList(response.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDolist(name=n)
            t.save()
        return HttpResponseRedirect("/%s" %t.name)
    else :
        form = CreateNewList()
    return render(response, "main/create.html", {"form":form,"l":l})

def view1 (response):
    l = ToDolist.objects.all()
    return render(response, "main/home.html", {"l":l})

def index (response,name):
    l = ToDolist.objects.all()
    ls = ToDolist.objects.get(name=name)
    #items = ls.item_set.all()
    #return HttpResponse("<h1>%s</h1><br></br><p>%s</p><p>%s</p>" %(ls.name,items[0].text,items[1].text))
    #return HttpResponse("<h1>%s</h1>" %ls.name)
    if response.method == "POST" :
       # print(response.POST)
        if response.POST.get("save"):
            for item in ls.item_set.all():
                if response.POST.get("c" + str(item.id)) == "clicked":
                    item.complete = True
                else :
                    item.complete = False
                item.save()
        if response.POST.get("newItem"):
            txt = response.POST.get("new")
            if len(txt) > 0 :
                ls.item_set.create(text = txt, complete = False)
            else :
                print("invalid text")
    return render(response, "main/list.html", {"ls":ls, "l":l})