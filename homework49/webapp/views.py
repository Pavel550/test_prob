from django.shortcuts import render


# Create your views here.

def my_blog(request):

    return  render(request, "my_blog.html")


def my_projekt(request):

    return  render(request, "my_projekt.html")