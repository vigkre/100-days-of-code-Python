import requests
from bs4 import BeautifulSoup

URL = "http://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
movies_web_page = response.text

soup = BeautifulSoup(movies_web_page, "html.parser")

movie_titles = [movie_title.get_text() for movie_title in soup.find_all(name="h3", class_="title")]

# # method 1: using slice
# movies = movie_titles[::-1]
# # method 2: using range
# for title in range(len(movie_titles)-1, -1, -1):
#     movies = movie_titles[::-1]
# method 3: using reversed function
# movies = reversed(movie_titles)

with open("movies.txt", "w", encoding="utf-8") as file:
    for title in reversed(movie_titles):
        file.write(title + "\n")
