import os

from flask import Flask, request, abort
from classes import InputData
from utils import FileDescriptor

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data/")

@app.route("/perform_query", methods=["GET", "POST"])
def perform_query():
    # filter, map, unique, sort, limit
    # получить параметры query и file_name из request.args, при ошибке вернуть ошибку 400
    # проверить, что файла file_name существует в папке DATA_DIR, при ошибке вернуть ошибку 400
    # с помощью функционального программирования (функций filter, map), итераторов/генераторов сконструировать запрос
    # вернуть пользователю сформированный результат

    if request.method == "GET":
        file_name = request.args.get('file_name', None)
        cmd1 = request.args.get('cmd1', None)
        value1 = request.args.get('value1', None)
        cmd2 = request.args.get('cmd2', None)
        value2 = request.args.get('value2', None)
    else:
        file_name = request.form.get('file_name', None)
        cmd1 = request.form.get('cmd1', None)
        value1 = request.form.get('value1', None)
        cmd2 = request.form.get('cmd2', None)
        value2 = request.form.get('value2', None)

    if not all([file_name, cmd1, value1, cmd2, value2]):
        abort(400)

    query = InputData(file_name=file_name, cmd1=cmd1, value1=value1, cmd2=cmd2, value2=value2)
    try:
        lines = FileDescriptor(query)
    except FileNotFoundError:
        return 'File not found', 400

    return app.response_class('', content_type="text/plain")


if __name__ == "__main__":
    app.run(debug=True)
