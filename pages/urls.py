
from django.urls import path
from . import views
urlpatterns = [
path("",views.index,name = "index"),
path("<int:movieId>",views.detail,name = "detail"),
path("categories/<int:category>",views.catMovie,name = "catMovie"),

]
