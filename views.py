from django.shortcuts import render
from django.shortcuts import (get_object_or_404, render, HttpResponseRedirect)
from django.http import HttpResponse

from . models import Books
from . forms import Booksform


def index(request):
    return HttpResponse("Hello, World. You are at the books index.")

def about(request):
    return HttpResponse("About Page")


def create_view(request):
    context = {}
    
    form = Booksform(request.POST or None)
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request,  "create_view.html", context)



def list_view(request):
	context ={}

	context["dataset"] = Books.objects.all()
		
	return render(request, "list_view.html", context)




def detail_view(request, id):

    context = {}

    context["data"] = Books.objects.get(id = id)

    return render(request, "detail_view.html", context)





def update_view(request, id):
	context ={}
	obj = get_object_or_404(Books, id = id)
	form = Booksform(request.POST or None, instance = obj)

	if form.is_valid():
		form.save()
		return HttpResponseRedirect("/"+id)

	context["form"] = form

	return render(request, "update_view.html", context)




def delete_view(request, id):
    context ={}

    obj = get_object_or_404(Books, id = id)


    if request.method =="POST":
        obj.delete()
        return HttpResponseRedirect("/")

    return render(request, "delete_view.html", context)
