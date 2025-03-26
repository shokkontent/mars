from flask import Flask, url_for, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


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


@app.route('/list_prof/<marking>')
def return_sample_marking(marking):
    prof = ['Разработчик Python', 'Data Scientist', 'Machine Learning Engineer', 'DevOps Engineer',
            'Full-Stack разработчик', 'Backend-разработчик', 'QA инженер', 'Системный администратор',
            'Специалист по кибербезопасности', 'Аналитик данных']
    return render_template('prof.html', prof=prof, marking=marking)


@app.route('/answer')
@app.route('/auto_answer')
def return_sample_answer():
    user = {'title': 'Анкета', 'surname': 'Василий', 'name': 'Ваня', 'education': 'Выше среднего',
            'profession': 'Повар', 'sex': 'male', 'motivation': 'Хочу и могу',
            'ready': 'True'}
    return render_template('auto_answer.html', user=user, title='dgsgsg',
                           css=url_for('static', filename='css/style.css'))


class LoginForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    photo = url_for('static', filename='img/emblem.png')
    return render_template('authorization.html', title='Аварийный доступ', form=form, photo=photo)


@app.route('/distribution')
def distribution():
    users = ['Дима', 'Вася', 'Петя', 'Таня', 'Маша', 'Варя', 'Геракл']
    return render_template('distribution.html', title='По каютам!', spisok_users=users)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
