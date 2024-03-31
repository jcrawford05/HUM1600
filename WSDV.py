# James Crawford
# 03/18/2024

"""
Web scrapping is copying data from the internet, with that, there is a constant issue with
copy write infringement, or the utilization of personal content, often without the original
authors knowledge or approval. There is the ethical qualm, in that when you data scrape, you
often aren't giving credit to the original author, so its almost as if you are plagiarizing
their work.
"""
import pandas as pd
# Imports
from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt
import numpy as np
import pandas as pn
import seaborn as sea


# Functions

def get_html_content(userURL):
    response = requests.get(userURL)
    if response.status_code == 200:
        return response.content
    else:
        return None


def dataScaper(html):
    """Function for Problem 1: This function takes an url and scrapes all urls from the given url"""
    soup = BeautifulSoup(html, 'html.parser')
    urlArray = [None] * len(soup.find_all('a'))
    i = 0
    for link in soup.find_all('a'):
        urlArray[i] = link.get('href')
        i += 1
    return urlArray


# Problem 1

url = 'https://en.wikipedia.org/wiki/Saturn_V'
linkArray = dataScaper(get_html_content(url))
print("The site has", len(linkArray), "links")

# Problem 2

"""Disclaimer: I used ChatGPT from OpenAI as a reference tool in the implementation of the polyfit function. 
Information like the order of the code and the variable names have been changed to fit the preexisting code.
"""

x = [2, 2, 3, 3, 7, 15, 15, 21, 21, 21, 22, 22, 24, 30, 33, 38, 39, 42, 47, 49, 51, 51, 52, 53, 55, 58, 59, 60,
     60, 61]
y = [-19.26, 12.19, 9.29, -9.51, 14.80, 11.23, 3.63, -1.08, 16.16, 3.45, -2.77, 7.46, 7.38, 15.66, 14.73,
     31.00, 26.48, 19.28, 14.42, 36.38, 33.35, 52.06, 28.63, 42.91, 32.10, 29.85, 14.40, 37.21, 21.56, 25.36]

plt.figure(figsize=(15, 5))
plt.subplot(1, 3, 1)
plt.plot(x, y, label='Line Graph', color='blue', linestyle='-')
plt.title('Line Graph')

plt.subplot(1, 3, 2)
plt.scatter(x, y, color='blue', label='Data Points')
plt.title('Scatter Plot')

plt.subplot(1, 3, 3)
plt.scatter(x, y, color='blue', marker='o', alpha=0.5)
coeff = np.polyfit(x, y, 1)
trendline_x = np.linspace(min(x), max(x), 100)
trendline_y = np.polyval(coeff, trendline_x)
plt.plot(trendline_x, trendline_y, color='red', linestyle='--', linewidth=2, label='Line of Best Fit')
plt.title('Scatter Plot with Line of Best Fit')

plt.grid(True)
plt.show()

# Problem 3

"""
Disclaimer: I used ChatGPT from OpenAI as a reference tool for the implementation of the pandas and seaborn libraries.
"""

data = {'TeamName': ['Reese', 'Barnes', 'Jones', 'Javez', 'Smith', 'Heath', 'Jacks', 'Weeks', 'Mitch', 'Rankle'],
        'HighestScore': [112, 103, 127, 99, 130, 107, 89, 120, 122, 90],
        'LowestScore': [47, 87, 70, 51, 100, 101, 38, 97, 110, 55]}

frame = pd.DataFrame(data)

plt.figure(figsize=(10, 6))
sea.lineplot(data=frame[['HighestScore', 'LowestScore']])
plt.title('Highest and Lowest Score per Team')
plt.xlabel('Team')
plt.ylabel('Score')
plt.xticks(range(len(frame["TeamName"])), frame['TeamName'], rotation=45) #This line was partailly written by chatGPT by OpenAI

plt.show()
