from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    # Lista 4 najpopularniejszych filmów z roku 2022
    movies = [
        {"title": "Spider-Man: No Way Home", "year": 2022, "genre": "Akcja/Przygodowy"},
        {"title": "Dune", "year": 2022, "genre": "Sci-Fi/Przygodowy"},
        {"title": "The Batman", "year": 2022, "genre": "Akcja/Dramat"},
        {"title": "Jurassic World: Dominion", "year": 2022, "genre": "Sci-Fi/Przygodowy"}
    ]
    return render_template("homepage.html", movies=movies)

if __name__ == '__main__':
    app.run(debug=True)