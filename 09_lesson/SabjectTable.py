from sqlalchemy import create_engine, text


class Database:
    def __init__(self, db_url):
        self.engine = create_engine(db_url)
        self._create_table()

    def _create_table(self):
        """Создаёт таблицу если её нет"""
        with self.engine.connect() as conn:
            conn.execute(text("""
                CREATE TABLE IF NOT EXISTS subject (
                    subject_id INTEGER PRIMARY KEY,
                    subject_title TEXT NOT NULL
                )
            """))
            conn.commit()

    def add_new_sabject(self, id, title):
        """Добавить предмет"""
        with self.engine.connect() as conn:
            conn.execute(
                text("INSERT INTO subject VALUES (:id, :title)"),
                {"id": id, "title": title}
            )
            conn.commit()

    def get_sabject(self, id):
        """Получить предмет по id"""
        with self.engine.connect() as conn:
            result = conn.execute(
                text("SELECT * FROM subject WHERE subject_id = :id"),
                {"id": id}
            )
            return result.fetchone()

    def update_sabject(self, id, new_title):
        """Обновить название предмета"""
        with self.engine.connect() as conn:
            conn.execute(
                text("UPDATE subject SET subject_title = :title WHERE subject_id = :id"),
                {"id": id, "title": new_title}
            )
            conn.commit()

    def delete_sabject_be_id(self, id):
        """Удалить предмет"""
        with self.engine.connect() as conn:
            conn.execute(
                text("DELETE FROM subject WHERE subject_id = :id"),
                {"id": id}
            )
            conn.commit()

    def clear(self, id):
        """Очистить тестовые данные"""
        with self.engine.connect() as conn:
            conn.execute(
                text("DELETE FROM subject WHERE subject_id = :id"), {"id": id})
            conn.commit()
