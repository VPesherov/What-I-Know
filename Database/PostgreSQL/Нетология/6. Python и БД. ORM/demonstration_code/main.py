import sqlalchemy
from sqlalchemy.orm import sessionmaker

from models import create_tables, Course, Homework

DSN = 'postgresql://postgres:123@localhost:5432/netology_db'
engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

course1 = Course(name='Python')
print(course1.id)

session.add(course1)
session.commit()
print(course1.id)

print(course1)

hw1 = Homework(number=1, description='дз1', course=course1)
hw2 = Homework(number=2, description='дз2', course=course1)

session.add_all([hw1, hw2])
session.commit()
session.close()
print('-' * 20)
for c in session.query(Course).all():
    print(c)
print('-' * 20)

for c in session.query(Homework).filter(Homework.number == 2).all():
    print(c)

print('-' * 20)

c2 = Course(name='Java')
session.add(c2)
session.commit()

subq = session.query(Homework).filter(Homework.description.like('%з%')).subquery()
iterable = session.query(Course).join(subq, Course.id == subq.c.course_id)

for c in iterable:
    print(c)

session.query(Course).filter(Course.name == 'Java').update({'name': 'JavaScript'})
session.commit()

session.query(Course).filter(Course.name == 'JavaScript').delete()
session.commit()

for c in session.query(Course).all():
    print(c)
