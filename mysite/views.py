from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import GeeksModel
from .forms import GeeksForm

def index(request):
    tasks = GeeksModel.objects.all()
    return render(request, 'mysite/index.html', {'tasks': tasks})

def add(request):
    context = {}
    if request.method == "POST":
        form = GeeksForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            img = form.cleaned_data.get("geeks_field")
            obj = GeeksModel.objects.create(
                title=name,
                img=img
            )
            obj.save()
            print(obj)
    else:
        form = GeeksForm()
    context["form"] = form
    return render(request, "mysite/add.html", context)
