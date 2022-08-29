import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.timeout.com/film/best-movies-of-all-time")
webPage = response.text
soup = BeautifulSoup(webPage, "html.parser")
allMovies = soup.findAll(name="h3", class_="_h3_cuogz_1")
movies = []
for movie in allMovies:
    movies.append(movie.getText())

with open(file="movies.txt", mode="w") as file:
    for movie in movies:
        file.write(movie.replace(" ", ""))
        file.write("\n")
