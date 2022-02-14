from django.shortcuts import render
from .movies import moviedb
from django.contrib import messages
# Create your views here.

moviedb = moviedb()
categories = moviedb.getcategories()["genres"]


def index(request):

    pagenumber = 1
    if request.method == "POST":
        if request.POST["type"] == "önceki":
            pagenumber = int(request.POST["pagenumber"])
            if pagenumber > 1:

                pagenumber -= 1

            # print(pagenumber)
        elif request.POST["type"] == "sonraki":
            pagenumber = int(request.POST["pagenumber"])

            pagenumber += 1

    trendMovies = moviedb.trendMovies(pagenumber)["results"]

    context = {
        "pagenumber": pagenumber,
        "movies": trendMovies,
        "categories": categories,
    }

    return render(request, "pages/index.html", context)


def detail(request, movieId):
    detail = moviedb.getDetailByıd(movieId)
    context = {
        "detail": detail,
        "categories": categories,
    }

    return render(request, "pages/detail.html", context=context)


def catMovie(request, category):
    pagenumber = 1
    if request.method == "POST":
        if request.POST["type"] == "önceki":
            pagenumber = int(request.POST["pagenumber"])
            if pagenumber > 1:

                pagenumber -= 1

            # print(pagenumber)
        elif request.POST["type"] == "sonraki":
            pagenumber = int(request.POST["pagenumber"])

            pagenumber += 1

   

    moviesByCategories = moviedb.getmoviesByCategories(category,pageNumber=pagenumber)["results"]

    # for title
    for a in categories:
        if (category == a["id"]):
            currentcategory = a["id"]
            title = a["name"]

    context = {
        'pagenumber': pagenumber,
        'movies': moviesByCategories,
        "categories": categories,
        'title': title,
        'currentcategory':currentcategory,
    }

    return render(request, "pages/category.html", context)
