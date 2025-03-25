from flask import Flask, url_for, render_template

app = Flask(__name__)


@app.route('/image_mars')
def return_fsample_page():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                  <img src="{url_for('static', filename='img/MARS.png')}" 
           alt="здесь должна была быть картинка, но не нашлась">
                    <div class="alert alert-primary" role="alert">
                      На ней много ресурсов;
                    </div>
                    <div class="alert alert-secondary" role="alert">
                      Та ней есть вода и атмосфера;
                    </div>
                    <div class="alert alert-success" role="alert">
                      Там есть магнитное поле;
                    </div>
                    <div class="alert alert-warning" role="alert">
                      Наконец, она просто красивая!
                  </body>
                </html>"""


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def retuvrn_sample_page(nickname, level, rating):
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <title>Варианты выбора</title>
                  </head>
                  <body>
                    <h1>Результаты отбора</h2>
                  </div>
                    Претендента на участие в миссии {nickname}:</h1>
                    <div class="alert alert-primary" role="alert">
                      Поздравляем! Ваш рейтинг после {level} этапа отбора
                    </div>
                      Составляет {rating}!</h1>
                    </div>
                    <div class="alert alert-success" role="alert">
                      Желаем удачи!
                    </div>
                  </body>
                </html>"""


@app.route('/<title>')
@app.route('/image_mars/<title>')
def return_sample_page(title):
    return render_template('base.html', title=title)


@app.route('/training/<prof>')
def return_sample_prof(prof):
    if prof in 'Инженер' or prof in 'строитель':
        title = 'Инженерные тренажеры'
        photo = url_for('static', filename='img/корабль1.jpg')
    else:
        title = 'Научные симуляторы'
        photo = url_for('static', filename='img/корабль2.jpg')
    return render_template('ship.html', title=title, photo=photo)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
