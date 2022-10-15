from flask_restx import Api

from project.views import auth_ns
from project.views.directors import directors_ns
from project.views.genres import genres_ns
from project.views.movies import movies_ns
from project.views.users import users_ns

from project.config import DevelopmentConfig
from project.dao.models import Genre, User, Director, Movie
from project.server.server import db

def create_app(config_objects):
    from flask import Flask
    app = Flask(__name__)
    app.config.from_object(config_objects)
    register_extensions(app)
    return app

def register_extensions(app):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(directors_ns)
    api.add_namespace(movies_ns)
    api.add_namespace(genres_ns)
    api.add_namespace(users_ns)
    api.add_namespace(auth_ns)

app = create_app(DevelopmentConfig)


@app.shell_context_processor
def shell():
    return {
        "db": db,
        "Genre": Genre,
        "User": User,
        "Director": Director,
        "Movie": Movie,
    }


if __name__ == '__main__':
    app.run(port=8000)