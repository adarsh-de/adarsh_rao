from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html')
def gallery(request):
    return render(request,'gallery.html')
def songs(request):
    return render(request,'songs.html')
def favourite (request):
    return render(request,'favourite.html')
def family (request):
    return render(request,'family.html')
def special(request):
    return render(request,'special.html')
def foods (request):
    return render(request,'foods.html')
def friends (request):
    return render(request,'friends.html')
def pictures (request):
    return render(request,'pictures.html')
def movie (request):
    return render(request,'movie.html')

