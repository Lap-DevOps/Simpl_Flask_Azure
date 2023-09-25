from flask import Flask, render_template, current_app

app = Flask(__name__)


@app.route('/')
def home():
    flask_ins= current_app
    return render_template('home.html', current_app=flask_ins)


if __name__ == '__main__':
    app.run(debug=True)
