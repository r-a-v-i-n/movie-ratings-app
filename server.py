"""Server for movie ratings app."""

from flask import (Flask, render_template, request, flash, session,
                   redirect)
from model import connect_to_db
import crud

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def homepage():
    return render_template('homepage.html')


@app.route('/movies')
def all_movies():
    """View all movies."""

    movies = crud.list_movies()

    return render_template('all_movies.html', movies = movies)

@app.route('/movies/<movie_id>')
def show_movie(movie_id):
    """Show details on a particular movie."""
    get_movie = crud.get_movie_by_id(movie_id)

    return render_template('movie_details.html', get_movie=get_movie)


# Replace this with routes and view functions!


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
