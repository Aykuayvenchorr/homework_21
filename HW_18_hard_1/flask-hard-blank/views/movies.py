# здесь контроллеры/хендлеры/представления для обработки запросов (flask ручки). сюда импортируются сервисы из пакета service

# Пример
from flask_restx import Resource, Namespace
from flask import request
from dao.model.schema import MovieSchema
from implemented import movie_service

movie_ns = Namespace('movies')
movies_schema = MovieSchema(many=True)


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        director_id = request.args.get("director_id")
        genre_id = request.args.get('genre_id')
        year = request.args.get('year')
        if director_id and genre_id and year:
            return movies_schema.dump((movie_service.get_movie_by(director_id=director_id,
                                                                  genre_id=genre_id,
                                                                  year=year)))
        elif director_id:
            return movies_schema.dump(movie_service.get_movie_by(director_id=director_id))
        elif genre_id:
            return movies_schema.dump(movie_service.get_movie_by(genre_id=genre_id))
        elif year:
            return movies_schema.dump(movie_service.get_movie_by(year=year))
        else:
            return movies_schema.dump(movie_service.get_movies()), 200

    def post(self):
        movie_service.add_movie(request.json)
        return "ok", 201


@movie_ns.route('/<int:id>')
class MovieView(Resource):
    def get(self, id):
        return movies_schema.dump([movie_service.get_movie_by(id=id)]), 200

    def put(self, id):
        movie_service.update_movie(request.json)
        return "ok", 201

    def delete(self, id):
        movie_service.delete_movie_by_id(id)
        return 'ok', 201
