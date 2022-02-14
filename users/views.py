from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from pages.models import movie_infos
from pages.movies import moviedb
from django.contrib import messages
# Create your views here.


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        repassword = request.POST["repassword"]
        email = request.POST["email"]

        if len(password) > 7:
            print("parolar yeterince uzun. ")
            if password == repassword:
                
               

                if(User.objects.filter(username=username).exists()):
                    print("eşleşen biri var ")
                    messages.add_message(request, messages.WARNING, 'eşleşen biri var')
                else:
                    print("kişi başarıyla oluşturuldu")
                    messages.add_message(request, messages.SUCCESS, 'kişi başarıyla oluşturuldu')
                    
                    User.objects.create_user(
                        username=username, email=email, password=password)
                    return redirect("index")

            else:
                print("parolalar eşleşmiyor")
                messages.add_message(request, messages.WARNING, "parolalar eşleşmiyor")
                

        else:
            print("parlola kısa ")
            messages.add_message(request, messages.WARNING, "parola kısa ")

    return render(request, "users/register.html")


def login(request):
    if request.method == "POST":
        
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.add_message(request, messages.SUCCESS, ' başarıyla giriş yapıldı ')
            return redirect("index")

    return render(request, 'users/login.html')


def logout(request):
    if request.method == "POST":
        auth.logout(request)
        messages.add_message(request, messages.SUCCESS, f'başarıyla çıkış yapıldı')    
        
        return redirect("index")

movie = moviedb()
categories = movie.getcategories()["genres"]


def addFavorite(request):
    if request.method == "POST":
        movie_id = request.POST["movie_id"]
        path = request.POST["path"]
        title = request.POST["title"]

        print(movie_id, path, title)

        if (movie_infos.objects.filter(movieıd=movie_id, user=User.objects.get(username=request.user.username)).exists()) == False:

            print("aynı film değil devamke")

            obj = movie_infos.objects.create(
                movieıd=movie_id, path=path, title=title, user=User.objects.get(username=request.user.username))
            obj.save()
            messages.add_message(request, messages.SUCCESS, f'{title} filmi favorilere eklendi ')
        return redirect("index")
    context = {

        'movies': movie_infos.objects.filter(user=request.user.id),
        "categories": categories,
    }

    return render(request, 'users/favorite.html', context)


def deletefav(request):
    if request.method == "POST":
        movie_id = request.POST["id"]
        title = request.POST["title"]
        movie_infos.objects.filter(movieıd=movie_id).delete()
        messages.add_message(request, messages.SUCCESS, f'{title} adlı film favorilerinizden silindi.')

    return redirect("favorite")
