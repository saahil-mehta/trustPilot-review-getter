#!/usr/bin/env python
# coding: utf-8
"""
Created on: 2 August, 2023
Author: Saahil Mehta (saahil.mehta@digitas.com)
"""

# In[2]:


import requests
from bs4 import BeautifulSoup
import json
import pandas as pd


# In[6]:


def fetch_reviews(brand, pages_to_fetch):
    """
    Fetches reviews of the given brand from Trustpilot.com and returns a DataFrame of the fetched reviews.

    Developed by: Saahil Mehta (saahil.mehta@digitas.com)

    This function iterates over specified number of pages and scrapes review data. Each review data contains
    fields: 'id', 'itemReviewed', 'author', 'datePublished', 'headline', 'reviewBody', and 'reviewRating'.
    
    This can be utilized by different pitching teams to draw company specific data for their pitches.
    By providing the company name (brand) and specifying the number of pages to fetch, teams can get a 
    considerable amount of review data.

    Parameters:
    brand (str): The brand for which reviews are to be fetched.
    pages_to_fetch (int): The number of pages of reviews to fetch.

    Returns:
    DataFrame: A pandas DataFrame containing the reviews.
    
    Example:
    >>> brand = "axainsurance.co.uk"
    >>> pages_to_fetch = 2
    >>> df = fetch_reviews(brand, pages_to_fetch)
    """

    all_reviews = []

    for i in range(1, pages_to_fetch+1):
        response = requests.get(f"https://www.trustpilot.com/review/{brand}?page={i}")
        html_content = response.text

        soup = BeautifulSoup(html_content, "html.parser")
        script_tag = soup.find('script', {'type':'application/ld+json'})
        data = json.loads(script_tag.string)

        reviews = []
        try:
            for item in data['@graph']:
                if item['@type'] == 'LocalBusiness':
                    for review in item['review']:
                        review_id = review['@id']
                        for review_item in data['@graph']:
                            if review_item['@id'] == review_id:
                                review_info = {
                                    'id': review_id,
                                    'itemReviewed': review_item['itemReviewed']['@id'],
                                    'author': review_item['author']['name'],
                                    'datePublished': review_item['datePublished'],
                                    'headline': review_item['headline'],
                                    'reviewBody': review_item['reviewBody'],
                                    'reviewRating': review_item['reviewRating']['ratingValue'],
                                }
                                reviews.append(review_info)
        except KeyError:
            print(f"No reviews found for brand: {brand} and page {i}.")
            continue
        all_reviews.extend(reviews)

    return pd.DataFrame(all_reviews)


# In[7]:


brand = "www.perrigo.com"
pages_to_fetch = 1
data = fetch_reviews(brand, pages_to_fetch)


# In[10]:


brand = "www.mojainsurance.co.uk"
pages_to_fetch = 30
data = fetch_reviews(brand, pages_to_fetch)


# In[12]:


# data.to_csv("mojaTrustpilot.csv")


# In[ ]:




