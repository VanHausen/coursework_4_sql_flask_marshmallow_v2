from project.dao import MovieDAO
from project.exceptions import ItemNotFound
from project.schemas.movie import MovieSchema
from project.services.base import BaseService


class MoviesService(BaseService):
    # def __init__(self, dao: MovieDAO):
    #     self.dao = dao
    def get_item_by_id(self, pk):
        movie = MovieDAO(self._db_session).get_by_id(pk)
        if not movie:
            raise ItemNotFound
        return MovieSchema().dump(movie)

    def get_all_movies(self):
        movies = MovieDAO(self._db_session).get_all()
        return MovieSchema(many=True).dump(movies)

    def create(self, movie_d):
        movie = MovieDAO(self._db_session).create(movie_d)
        return MovieSchema(many=True).dump(movie)


    def update(self, movie_d):
        movies = MovieDAO(self._db_session).update(movie_d)
        return MovieSchema().dump(movies)

    def delete(self, rid):
        MovieDAO(self._db_session).delete(rid)


        #
        # movies = MovieDAO(self._db_session).get_all()
        # return MovieSchema(many=True).dump(movies)