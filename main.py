import requests
from bs4 import BeautifulSoup
import pandas as pd
from tabulate import tabulate

number_of_articles = 5  # Number of articles that we want to retrieve
headline_list = []
intro_list = []
full_list = []  # Empty list that is going to be used for future iteration of the project***

# Creating a loop in order to gain the 5 most popular
# headlines on the BBC news business page
for n in range(0, number_of_articles):
    url = "https://www.bbc.co.uk/news/business"   # The URL of the website that the data is being retrieved from
    page = requests.get(url)  # Get access to the BBC business news page

    soup = BeautifulSoup(page.content, 'html.parser')  # Get the HTML content of the page

    headlines = soup.find_all('a', class_="gs-c-promo-heading")  # Find all headline titles through HTML classes
    intro = soup.find_all('p', class_="gs-c-promo-summary")  # Find all headline intros through HTML classes

    title = headlines[n].get_text()  # Assigning the headline text to the 'title' variable
    headline_list.append(title)
    paragraph = intro[n].get_text()
    intro_list.append(paragraph)    # Adding the text of the headline to the list

df = pd.DataFrame(  # Creating a dataframe in order to display the collected data from the site.
    {'Article Title': headline_list,  # Creating two columns in the dataframe one displaying all the Article Titles
     'Article Info': intro_list}  # the other displaying all the intros to the article.
)

pd.set_option('display.max_colwidth', None)  # No max length to the columns, allowing for long intros if need be
pd.set_option('display.colheader_justify', "left")  # Set the column headers to the left of the dataframe

# prints the titles and intros to the top 5 articles using the tabulate library, keeping it neat in a fancy grid
print(tabulate(df, showindex=False, headers=df.columns, tablefmt='fancy_grid'))

