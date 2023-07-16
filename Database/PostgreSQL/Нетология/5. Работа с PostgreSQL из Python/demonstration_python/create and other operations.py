import psycopg2

with psycopg2.connect(database="netology_db", user="postgres", password="123") as conn:
    with conn.cursor() as cur:
        # удаление таблиц
        cur.execute("""
        DROP TABLE homework;
        DROP TABLE course;
        """)

        # создание таблиц
        cur.execute("""
        CREATE TABLE IF NOT EXISTS course(
            id SERIAL PRIMARY KEY,
            name VARCHAR(40) UNIQUE
        );
        """)
        cur.execute("""
                CREATE TABLE IF NOT EXISTS homework(
                    id SERIAL PRIMARY KEY,
                    number INTEGER NOT NULL,
                    description TEXT NOT NULL,
                    course_id INTEGER NOT NULL REFERENCES course(id)
                );
                """)
        conn.commit()

        # наполнение таблиц (C из CRUD)
        cur.execute("""
                INSERT INTO course(name) VALUES('Python');
                """)
        conn.commit()  # фиксируем в БД

        cur.execute("""
                INSERT INTO course(name) VALUES('Java') RETURNING id, name;
                """)
        print(cur.fetchone())  # запрос данных автоматически зафиксирует изменения

        # извлечение данных (R из CRUD)
        cur.execute("""
                SELECT * FROM course;
                """)
        print('fetchall', cur.fetchall())  # извлечь все строки

        cur.execute("""
                SELECT * FROM course;
                """)
        print(cur.fetchone())  # извлечь первую строку (аналог LIMIT 1)

        cur.execute("""
                SELECT * FROM course;
                """)
        print(cur.fetchmany(3))  # извлечь первые N строк (аналог LIMIT N)

        cur.execute("""
                SELECT name FROM course;
                """)
        print(cur.fetchall())

        print('-'*20)

        cur.execute("""
              SELECT id FROM course WHERE name='Python';
              """)
        print(cur.fetchone())

        cur.execute("""
              SELECT id FROM course WHERE name='{}';
              """.format("Python"))  # плохо - возможна SQL инъекция
        print(cur.fetchone())

        cur.execute("""
              SELECT id FROM course WHERE name=%s;
              """, ("Python",))  # хорошо, обратите внимание на кортеж
        print(cur.fetchone())


        def get_course_id(cursor, name: str) -> int:
            cursor.execute("""
            SELECT id FROM course WHERE name=%s;
            """, (name,))
            return cur.fetchone()[0]


        python_id = get_course_id(cur, 'Python')
        print('python_id', python_id)