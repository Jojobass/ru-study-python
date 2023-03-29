from flask import Flask, request


user_data: dict[str, dict] = dict()


class FlaskExercise:
    """
    Вы должны создать API для обработки CRUD запросов.
    В данной задаче все пользователи хранятся в одном словаре, где ключ - это имя пользователя,
    а значение - его параметры. {"user1": {"age": 33}, "user2": {"age": 20}}
    Словарь (dict) хранить в памяти, он должен быть пустым при старте flask.

    POST /user - создание пользователя.
    В теле запроса приходит JSON в формате {"name": <имя пользователя>}.
    Ответ должен вернуться так же в JSON в формате {"data": "User <имя пользователя> is created!"}
    со статусом 201.
    Если в теле запроса не было ключа "name", то в ответ возвращается JSON
    {"errors": {"name": "This field is required"}} со статусом 422

    GET /user/<name> - чтение пользователя
    В ответе должен вернуться JSON {"data": "My name is <name>"}. Статус 200

    PATCH /user/<name> - обновление пользователя
    В теле запроса приходит JSON в формате {"name": <new_name>}.
    В ответе должен вернуться JSON {"data": "My name is <new_name>"}. Статус 200

    DELETE /user/<name> - удаление пользователя
    В ответ должен вернуться статус 204
    """

    @staticmethod
    def configure_routes(app: Flask) -> None:
        global user_data
        user_data = dict()
        app.add_url_rule("/user", view_func=FlaskExercise.create_user, methods=["POST"])
        app.add_url_rule("/user/<name>", view_func=FlaskExercise.get_user_data, methods=["GET"])
        app.add_url_rule("/user/<name>", view_func=FlaskExercise.patch_user_data, methods=["PATCH"])
        app.add_url_rule("/user/<name>", view_func=FlaskExercise.delete_user, methods=["DELETE"])

    @staticmethod
    def create_user() -> tuple[dict, int]:
        request_ = request.json
        if "name" in request_:
            global user_data
            user_data[request_["name"]] = {}
            return {"data": f"User {request_['name']} is created!"}, 201
        return {"errors": {"name": "This field is required"}}, 422

    @staticmethod
    def get_user_data(name: str) -> tuple[dict, int]:
        global user_data
        if name in user_data:
            return {"data": f"My name is {name}"}, 200
        else:
            return {"errors": "Not found"}, 404

    @staticmethod
    def patch_user_data(name: str) -> tuple[dict, int]:
        request_ = request.get_json()
        global user_data
        if name in user_data:
            user_data[request_["name"]] = user_data[name]
            del user_data[name]
            return {"data": f"My name is {request_['name']}"}, 200
        else:
            return {"errors": "Not found"}, 404

    @staticmethod
    def delete_user(name: str) -> tuple[dict, int]:
        global user_data
        if name in user_data:
            del user_data[name]
            return {"data": f"User {name} is deleted"}, 204
        else:
            return {"errors": "Not found"}, 404
