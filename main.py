from bs4 import BeautifulSoup
import requests

response = requests.get(url='https://web.archive.org/web/20200518073855/https:/www.empireonline.com/movies/features/best-movies-2/')
webpage = response.text
soup = BeautifulSoup(webpage, 'html.parser')
all_movies = soup.find_all(name='h3', class_='title')
print(all_movies)
movie_list = []
for movie in all_movies:
    movie_list.append(movie.getText())
print(movie_list)

updated_movie_list = []
for i in range(len(movie_list)-1, -1, -1):
    print(movie_list[i])
    updated_movie_list.append(movie_list[i])

with open('top_100_movies.txt',mode='w', encoding='utf-8') as file:
    for movie in updated_movie_list:
        file.write(f'{movie}\n')


