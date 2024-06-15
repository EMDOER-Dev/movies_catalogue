from flask import Flask, render_template, request
import tmdb_client
import random  # Dodaj to

app = Flask(__name__)

# Definicja context processor dla tmdb_image_url
@app.context_processor
def utility_processor():
    def tmdb_image_url(path, size='w342'):
        return tmdb_client.get_poster_url(path, size)
    return {'tmdb_image_url': tmdb_image_url}

# Endpoint dla strony głównej
@app.route('/')
def homepage():
    list_types = [
        {'key': 'popular', 'label': 'Filmy popularne'},
        {'key': 'now_playing', 'label': 'Filmy nowo wydane'},
        {'key': 'top_rated', 'label': 'Najwyżej oceniane filmy'},
        {'key': 'upcoming', 'label': 'Filmy nadchodzące'}
    ]
    selected_list = request.args.get('list_type', 'popular')
    
    # Sprawdzenie czy wybrany typ listy jest poprawny, jeśli nie, ustawiamy 'popular'
    valid_list_types = [list_type['key'] for list_type in list_types]
    if selected_list not in valid_list_types:
        selected_list = 'popular'
    
    movies = tmdb_client.get_movies_list(selected_list)
    return render_template('homepage.html', movies=movies, current_list=selected_list, list_types=list_types)

# Endpoint dla szczegółów filmu
@app.route("/movie/<movie_id>")
def movie_details(movie_id):
    details = tmdb_client.get_single_movie(movie_id)
    cast = tmdb_client.get_single_movie_cast(movie_id)
    movie_images = tmdb_client.get_movie_images(movie_id)
    selected_backdrop = random.choice(movie_images['backdrops']) if movie_images['backdrops'] else None
    return render_template("movie_details.html", movie=details, cast=cast, selected_backdrop=selected_backdrop)

if __name__ == '__main__':
    app.run(debug=True)