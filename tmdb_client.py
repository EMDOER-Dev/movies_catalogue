# tmdb_client.py

import requests

API_KEY = '0f214f28296c208dc3cf6d2dce154551'

# Funkcje do pobierania danych z API TMDB

def get_movies_list(list_type):
    endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
    params = {
        'api_key': API_KEY
    }
    try:
        response = requests.get(endpoint, params=params)
        response.raise_for_status()
        movies = response.json().get('results', [])

        for movie in movies:
            poster_path = movie.get('poster_path')
            if poster_path:
                movie['poster_url'] = get_poster_url(poster_path, 'w342')

        return movies
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    params = {
        'api_key': API_KEY
    }
    try:
        response = requests.get(endpoint, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching movie details: {e}")
        return None

def get_single_movie_cast(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    params = {
        'api_key': API_KEY
    }
    try:
        response = requests.get(endpoint, params=params)
        response.raise_for_status()
        return response.json()['cast']
    except requests.exceptions.RequestException as e:
        print(f"Error fetching cast data: {e}")
        return None

def get_movie_images(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/images"
    params = {
        'api_key': API_KEY
    }
    try:
        response = requests.get(endpoint, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching images data: {e}")
        return None

def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"