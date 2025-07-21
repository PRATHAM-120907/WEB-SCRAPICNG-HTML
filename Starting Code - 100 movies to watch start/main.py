import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 
response = requests.get(URL) # this line requests the owner of the site to get the data from the website

website_html = response.text # this line gets the HTML content of the website

soup = BeautifulSoup(website_html, "html.parser")# parse the HTML content using BeautifulSoup

all_movies = soup.find_all(name="h3" ,class_ ="title")# find all the movie titles in the HTML content
# the find_all method returns a list of all the elements that match the given criteria
# in this case, we are looking for all the h3 elements with the class "title

movies_titles = [movie.getText() for movie in all_movies]# this line extracts the text from each movie title element
# getText() method returns the text content of the element
# we use a list comprehension to create a list of movie titles

movies = movies_titles[::-1]# reverse the list of movie titles to get them in the correct order

with open("movies.txt" ,mode="w") as file:# open a file named "movies.txt" in write mode
    # this will create the file if it doesn't exist or overwrite it if it does
    # the mode "w" means write mode, which allows us to write to the file
    # we use a context manager (with statement) to ensure the file is properly closed after
    for movie in movies:
        file.write(f"{movie}\n")# write each movie title to the file
        # we use an f-string to format the string with the movie title
        # the "\n" at the end adds a new line after each movie title








