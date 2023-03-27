from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')  # Бедет обрабатывать два адреса
@app.route('/home')  # декоратор app для отслеживания адреса страницы
def index():  # put application's code here
    return render_template("index.html")



@app.route('/about')
def about():
    return render_template("about.html")


if __name__ == '__main__':
    app.run(debug=True)  # run запускает локальный сервер