import requests
from flask import redirect, render_template, request, session

api_key = "68b42ffd3343042e66ee1b940fad9eb0"
def lookup(type,page):

    # Contact API
    try:
        url = f"https://api.themoviedb.org/3/movie/{type}?api_key={api_key}&language=en-US&page={page}"
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException:
        return None
    
    # Parse response
    try:
        quote = response.json()
        return quote["results"]
    except (KeyError, TypeError, ValueError):
        return None


def lookmovie(id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{id}?api_key={api_key}&language=en-US"
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException:
        return None
    
    # Parse response
    try:
        quote = response.json()
        return quote
    except (KeyError, TypeError, ValueError):
        return None


def search(query,page):
    # Contact API
    try:
        url = f"https://api.themoviedb.org/3/search/movie?api_key={api_key}&language=en-US&query={query}&page={page}&include_adult=false"
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException:
        return None
    
    # Parse response
    try:
        quote = response.json()
        print(quote)
        return quote["results"]
    except (KeyError, TypeError, ValueError):
        return None