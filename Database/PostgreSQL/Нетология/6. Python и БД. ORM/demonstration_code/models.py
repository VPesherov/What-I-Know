import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Course(Base):
    # название таблица которая будет создана в postgres
    __tablename__ = "course"

    # далее создаём колонки
    # колонка id - колонка типа integer и с ограничением primary key
    id = sq.Column(sq.Integer, primary_key=True)
    # колонка name - тип строка с длиной 40 и с требованием уникальности
    name = sq.Column(sq.String(length=40), unique=True)
    # если же нам необходимы связи между таблицами то мы также можем их создать
    # с помощью вызова relationship
    # это свойство по которому можно связываться
    # homeworks = relationship("Homework", back_populates="course")

    def __str__(self):
        return f'{self.id}: {self.name}'


class Homework(Base):
    # название таблицы
    __tablename__ = "homework"

    # описываем столбцы, id
    id = sq.Column(sq.Integer, primary_key=True)
    # номер домашки
    number = sq.Column(sq.Integer, nullable=False)
    # описание домашки
    description = sq.Column(sq.Text, nullable=False)
    # курс к которому принадлежит домашнее задание
    # тут можно заметить как создаётся ограничения внешнего ключа - таблица.столбец
    course_id = sq.Column(sq.Integer, sq.ForeignKey("course.id"), nullable=False)

    # тут мы описываем с какой таблицей хотим связаться и описать какое обратное свойство будет связываться
    # с нами в данном случае это свойство homeworks
    # но такой вариант очень часто бывает недоубным, так как постоянно нужно будет менять код в обоих классах
    # course = relationship(Course, back_populates="homeworks")
    # поэтому посмотрим на второй вариант
    # но указываем уже не back_populates, а backref
    # backref - автоматических создаст свойство в связывании таблицы Course и создаст там свойство homeworks
    course = relationship(Course, backref="homeworks")

    def __str__(self):
        return f'{self.id}: {self.number}, {self.description}, {self.course_id}'


def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
