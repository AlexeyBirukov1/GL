from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return "Миссия Колонизация Марса"

@app.route('/index')
def countdown():
    countdown_list = []
    countdown_list.append('И на Марсе будут яблони цвести!')
    return '</br>'.join(countdown_list)

@app.route('/promotion')
def promotion():
    countdown_list = []
    countdown_list.append('Человечество вырастает из детства.')
    countdown_list.append('Человечеству мала одна планета.')
    countdown_list.append('Мы сделаем обитаемыми безжизненные пока планеты.')
    countdown_list.append('И начнем с Марса!')
    countdown_list.append('Присоединяйся!')
    return '</br>'.join(countdown_list)


@app.route('/image_mars')
def return_sample_page():
    return """<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="/static/img/mars.jpg" alt="здесь должна была быть картинка, но не нашлась">
                    <h6>Вот она красная планета!</h6>
                  </body>
                </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')