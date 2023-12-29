import pydantic
from flask import Flask, jsonify, request
from flask.views import MethodView
from models import Session, User
from schema import CreateUser, UpdateUser
from sqlalchemy.exc import IntegrityError

app = Flask('app')


def validate(schema_class, json_data):
    try:
        return schema_class(**json_data).dict(exclude_unset=True)
    except pydantic.ValidationError as er:
        error = er.errors()[0]
        error.pop("ctx", None)
        raise HttpError(400, error)


@app.before_request
def before_request():
    session = Session()
    request.session = session


@app.after_request
def after_request(response):
    request.session.close()
    return response


class HttpError(Exception):
    def __init__(self, status_code: int, description: str):
        self.status_code = status_code
        self.description = description


@app.errorhandler(HttpError)
def error_handler(error: HttpError):
    response = jsonify({"error": error.description})
    response.status_code = error.status_code
    return response


def get_user_by_id(user_id: int):
    user = request.session.get(User, user_id)
    if user is None:
        raise HttpError(404, "user not found")
    return user


def add_user(user: User):
    try:
        request.session.add(user)
        request.session.commit()
    except IntegrityError:
        raise HttpError(400, "user arleadt exists")

class UserView(MethodView):

    def get(self, user_id):
        user = get_user_by_id(user_id)
        return jsonify(user.dict_)

    def post(self):
        json_data = validate(CreateUser, request.json)
        user = User(**json_data)
        add_user(user)
        print(user.id, user.name, user.registration_time)
        return jsonify(user.dict_)

    def patch(self, user_id):
        json_data = validate(UpdateUser, request.json)
        user = get_user_by_id(user_id)
        for key, value in json_data.items():
            setattr(user, key, value)
        add_user(user)
        return jsonify(user.dict_)

    def delete(self, user_id):
        user = get_user_by_id(user_id)
        request.session.delete(user)
        request.session.commit()
        return jsonify(
            {
                "status": "deleted",
            }
        )


def hello_world():
    json_data = request.json
    print(f'{json_data}')
    qs = request.args
    print(f'{qs=}')
    headers = request.headers
    print(f'{headers=}')
    response = jsonify({"hello": "world"})
    return response


app.add_url_rule("/hello/world", view_func=hello_world, methods=["POST"])

user_view = UserView.as_view("user")
app.add_url_rule("/user/", view_func=user_view, methods=["POST"])
app.add_url_rule("/user/<int:user_id>", view_func=user_view, methods=["GET", "PATCH", "DELETE"])

app.run()
