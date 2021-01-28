import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import re

# A function to collect lego sets from search results on brickset.com
def collectLegoSets(startURL):
    # Retrieve starting URL
    myPage = requests.get(startURL)

    # Parse the website with Beautiful Soup
    parsed = BeautifulSoup(myPage.text)
    
    # Grab all sets from the page
    a = [i for i in parsed.find_all('article')]

    # Create and empty data set
    newData = []

    # Iterate over all sets on the page
    for i in a:
        row = []
        # Add the set name to the row of data
        row.append(i.h1.text)
        try:
            # Extract price and translate to a floating point number from string, append to row IF PRICE EXISTS
            row.append(float(re.search(r'(\d+.\d+)(\u20AC)', i.find('dt', text="RRP").find_next_sibling().text, re.UNICODE).groups()[0]))
        except:
            # Missing value for sets with no price, append to row IF NO PRICE EXISTS
            row.append(np.nan)
            
        try:
            row.append(int(i.find('dt', text="Pieces").find_next_sibling().text))
        except:
            # Missing value for sets with no pieces info
            row.append(np.nan)
            
        try:
            row.append(int(i.find('dt', text="Minifigs").find_next_sibling().text))        
        except:
            # Missing value for sets with no minifigs info
            row.append(np.nan)
        
        # Add the row of data to the dataset
        newData.append(row)

    newData = pd.DataFrame(newData, columns = ['Set', 'Price_Euro', 'Pieces', 'Minifigs'])
    
    # Check if there are more results on the "next" page
    try:
        nextPage = parsed.find('li', class_="next").a['href']
    except:
        nextPage = None
    
    # If there is another page of results, grab it and combine
    if nextPage:
        return pd.concat([newData, collectLegoSets(nextPage)], axis=0).reset_index(drop=True)
    # Otherwise return the current data
    else:
        return newData
    
lego2019 = collectLegoSets("https://brickset.com/sets/year-2019")