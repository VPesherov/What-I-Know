import atexit
import datetime

from sqlalchemy import create_engine, String, DateTime, func
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, mapped_column

# задаём данные для подключения к бд
POSTGRES_USER = 'postgres'
POSTGRES_PASSWORD = '123'
POSTGRES_DB = 'test'
POSTGRES_HOST = '127.0.0.1'
POSTGRES_PORT = '5431'

# создаём подключение к бд
PG_DSN = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
engine = create_engine(PG_DSN)
# создаём сессию
Session = sessionmaker(bind=engine)

# это функция закроет подключение, если оно не закроется само
atexit.register(engine.dispose)



# наши модели/таблицы
class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "app_users"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    password: Mapped[str] = mapped_column(String(100), nullable=False)
    registration_time: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=func.now())

    @property
    def dict_(self):
        return {
            'id': self.id,
            'name': self.name,
            'registration_time': self.registration_time.isoformat(),
        }


Base.metadata.create_all(bind=engine)
