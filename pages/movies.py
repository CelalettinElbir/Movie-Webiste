import os
import requests
class moviedb:
    def __init__(self):
        self.apıKey = os.environ.get("HEAVENAPI")
        self.url = "https://api.themoviedb.org/3"


    def trendMovies(self,pagenumber):
        response = requests.get(f"{self.url}/movie/popular?api_key={self.apıKey}&language=tr&page={pagenumber}").json()
        return response


    def getDetailByıd(self,movie_id):
        response =requests.get(f"{self.url}/movie/{movie_id}?api_key={self.apıKey}&language=tr")
        return response.json() 


    def getcategories(self):
        response = requests.get(f"{self.url}/genre/movie/list?api_key={self.apıKey}&language=tr")
        return response.json()


    def getmoviesByCategories(self,category,pageNumber =1):
        response= requests.get(f"{self.url}/discover/movie?api_key={self.apıKey}&language=tr&sort_by=popularity.desc&page={pageNumber}&with_genres={category}").json()
        
            
        return response


      


