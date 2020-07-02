from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
@app.route('/entry')
def render() -> 'html':
    return render_template('entry.html',
                           tytul="Strona!")

@app.route('/log_to_file')
def log_to_file() -> 'file':
    pass
    #with open('data.log','a') as file
app.run(debug=True)