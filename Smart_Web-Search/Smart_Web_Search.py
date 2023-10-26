# Smart_Web_Search

# 🔎 Accumulating and Google web search words.

# Copyright (C) 2023, Sourceduty - All Rights Reserved.
# THE CONTENTS OF THIS PROJECT ARE PROPRIETARY.


import os
import requests
from bs4 import BeautifulSoup
import random

# Initialize the search history file
search_history_file = 'search_history.txt'

# Function to perform a web search
def search_web(query):
    search_url = f"https://www.google.com/search?q={query}"
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    headers = {"User-Agent": user_agent}

    try:
        response = requests.get(search_url, headers=headers)
        if response.status_code == 200:
            return response.text
    except Exception as e:
        print(f"Error: {e}")

    return None

# Function to accumulate search words from the search history file
def accumulate_search_words():
    search_words = set()
    if os.path.exists(search_history_file):
        with open(search_history_file, 'r') as file:
            lines = file.read().splitlines()
            search_words.update(lines)
    return list(search_words)

# Function to update the search history file
def update_search_history(query):
    search_words = accumulate_search_words()
    search_words.append(query)
    with open(search_history_file, 'w') as file:
        file.write('\n'.join(search_words))

# Main program
if __name__ == "__main__":
    # Accumulate search words from the history
    accumulated_words = accumulate_search_words()

    if accumulated_words:
        print("Your previous search terms:")
        for word in accumulated_words:
            print(word)
    else:
        print("No search history available.")

    # Get user input for the search query
    search_query = input("Enter your search query: ")

    # Perform the web search
    search_result = search_web(search_query)

    if search_result:
        # Parse the search results (you may need to customize this for your use case)
        soup = BeautifulSoup(search_result, 'html.parser')
        search_results = soup.find_all("h3")
        print("Search Results for:", search_query)
        for index, result in enumerate(search_results, start=1):
            print(f"{index}. {result.text}\n")

        # Update the search history with the current search query
        update_search_history(search_query)
    else:
        print("Failed to perform the web search.")
