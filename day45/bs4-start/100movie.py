from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")

movie_page_soup = BeautifulSoup(response.text, "html.parser")
#print(movie_page_soup.prettify())

movie_titles = [title.getText() for title in movie_page_soup.find_all(name="h3", class_="title")]
movies = movie_titles[::-1]

with open('movies_title.txt', 'w', newline='') as file:
    for title in movies:
        file.write(title + "\n")

# print(movie_titles)
#
# with open('movies_title.txt', 'w', newline='') as file:
#     for i in range(len(movie_titles)):
#         movie_title = movie_titles[100 - i - 1]
#         movie_title = (" ").join(movie_title)
#         file.write(str(i + 1) + ") " + movie_title  + "\n")


