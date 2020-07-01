from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/entry')
def render() -> 'html':
    return render_template('entry.html',
                           tytul="Strona!")


app.run()
