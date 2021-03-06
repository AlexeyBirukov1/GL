import datetime
import sqlalchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from .db_session import SqlAlchemyBase
from sqlalchemy import orm

# наследуем от объекта класса SqlAlchemyBase
class User(SqlAlchemyBase, UserMixin):
    # можно указать имя создаваемой таблицы
    __tablename__ = 'users'
    # описание столбцов
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    about = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    email = sqlalchemy.Column(sqlalchemy.String,
                              index=True, unique=True, nullable=True)
    hashed_password = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    created_date = sqlalchemy.Column(sqlalchemy.DateTime,
                                     default=datetime.datetime.now)

    news = orm.relation("News", back_populates='user')

    # вывод пользователя с заданными параметрами
    def __repr__(self):
        return f'<User> {self.id} {self.name} {self.email}'

    #  устанавливает значение хэша пароля для переданной строки
    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)
    # проверяет, правильный ли пароль ввел пользователь
    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)