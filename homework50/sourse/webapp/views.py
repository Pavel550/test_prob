from django.shortcuts import render, HttpResponseRedirect
from webapp.cat_form import CatForm
from webapp.cat import Cat

# Create your views here.


def simulator(request):
    if request.method == "GET":
        return render(request, "simulator.html")
    else:
        cat_name = request.POST.get("cat_name")
        Cat.name = cat_name
        return HttpResponseRedirect('cat_stats/')

def cat_stats(request):
    if request.method == "GET":
        context = {"name": Cat.name, "age": Cat.age, "happy": Cat.happy, "hungry": Cat.hungry, "avatar": Cat.avatar}
        return render(request, "cat_stats.html", context)
    else:
        cat_name = request.POST.get("cat_name")
        Cat.name = cat_name
        return HttpResponseRedirect('cat_stats/')


        action = request.POST.get('action')
        if action == 'feed':
            cat.feed()
        elif action == 'play':
            cat.play()
        elif action == 'sleep':
            cat.sleeping()
    return HttpResponseRedirect('cat_stats/')



