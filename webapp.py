from flask import Flask, render_template, request, redirect, escape
import datetime
app = Flask(__name__)


@app.route('/')
@app.route('/entry')
def render() -> 'html':
    return render_template('entry.html',
                           tytul="Strona!")


@app.route('/log_to_file', methods=['POST'])
def log_to_file() -> 'redirect':
    lista: list = []
    with open('data.log', 'a') as log_file:
        string_to_inject = ""
        print(datetime.datetime.now() ,file=log_file, end=" | ")
        print("[", end='', file=log_file)
        for i in request.form:
            string_to_inject += escape(request.form[i]) + ","
        string_to_inject = string_to_inject[:-1]
        print(string_to_inject, file=log_file, end="")
        print("]", end='', file=log_file)
        print(file=log_file)
    return redirect('/')


app.run(debug=True)
