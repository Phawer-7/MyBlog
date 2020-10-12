from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy  # подключение модуля для работы с бд
from datetime import datetime

# https://www.youtube.com/watch?v=G-si1WbtNeM&t=972s видео на ютуб 17 43

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# класс для создания старниц в блоге
class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    intro = db.Column(db.String(300), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Article %r>' % self.id


# главная страница в ссылках home и в обычной
@app.route('/')
@app.route('/home')
def index():
    # используем хтмл файл, то есть к главным страницам соединяем файл index.html
    return render_template('index.html')


# ссылка about
@app.route('/about')
def about_page():
    return render_template('about.html')


@app.route('/create-article', methods=['POST', 'GET'])
def create_article():
    # if
    return render_template('create-article.html')


if __name__ == '__main__':
    app.run(debug=True)
    # дебаг мод, показывает ошибки сразу на странице, перед деплоем на сервер это надо изменить на False
