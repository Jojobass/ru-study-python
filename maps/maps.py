from typing import Union


class MapExercise:
    @staticmethod
    def rating(list_of_movies: list[dict]) -> float:
        """
        !!Задание нужно решить используя map!!
        Посчитать средний рейтинг фильмов (rating_kinopoisk) у которых две или больше стран.
        Фильмы у которых рейтинг не задан или равен 0 не учитывать в расчете среднего.

        :param list_of_movies: Список фильмов.
        Ключи словаря: name, rating_kinopoisk, rating_imdb, genres, year, access_level, country
        :return: Средний рейтинг фильмов у которых две или больше стран
        """

        def process_movie(movie: dict) -> float:
            if movie["rating_kinopoisk"] and len(movie["country"].split(",")) > 1:
                return float(movie["rating_kinopoisk"])
            return 0.0

        ratings = map(process_movie, list_of_movies)
        num_movies = 0
        total_rating = 0.0
        for rating in ratings:
            if rating >= 1:
                num_movies += 1
                total_rating += rating
        if num_movies:
            return total_rating / num_movies
        return 0.0

    @staticmethod
    def chars_count(list_of_movies: list[dict], rating: Union[float, int]) -> int:
        """
        !!Задание нужно решить используя map!!
        Посчитать количество букв 'и' в названиях всех фильмов с рейтингом (rating_kinopoisk) больше
        или равным заданному значению

        :param list_of_movies: Список фильмов
        Ключи словаря: name, rating_kinopoisk, rating_imdb, genres, year, access_level, country
        :param rating: Заданный рейтинг
        :return: Количество букв 'и' в названиях всех фильмов с рейтингом больше
        или равным заданному значению
        """

        def process_movie(movie: dict) -> int:
            if (
                movie["rating_kinopoisk"]
                and float(movie["rating_kinopoisk"]) >= rating
                and movie["name"]
            ):
                return movie["name"].count("и")
            return 0

        counts = map(process_movie, list_of_movies)
        return sum(counts)
