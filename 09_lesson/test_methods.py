from SabjectTable import Database

DB_URL = "postgresql://postgres:123@localhost:5432/Lesson_9"
TEST_ID = 999
TEST_NAME = "Математика"
NEW_NAME = "Физика"


db = Database(DB_URL)


def setup_function():
    """Выполняется перед КАЖДЫМ тестом - очищаем старые данные"""
    db.clear(TEST_ID)


def teardown_function():
    """Выполняется после КАЖДОГО теста - удаляем созданные данные"""
    db.clear(TEST_ID)


def test_add_new_sabject():
    """Тест добавления предмета"""
    # Добавляем
    db.add_new_sabject(TEST_ID, TEST_NAME)

    # Проверяем
    result = db.get_sabject(TEST_ID)
    assert result is not None
    assert result[1] == TEST_NAME


def test_update_sabject():
    """Тест изменения предмета"""
    # добавляем
    db.add_new_sabject(TEST_ID, TEST_NAME)

    # Изменяем
    db.update_sabject(TEST_ID, NEW_NAME)

    # Проверяем
    result = db.get_sabject(TEST_ID)
    assert result[1] == NEW_NAME
    assert result[1] != TEST_NAME


def test_delete_sabject():
    """Тест удаления предмета"""
    # добавляем
    db.add_new_sabject(TEST_ID, TEST_NAME)

    # Проверяем что добавилось
    assert db.get_sabject(TEST_ID) is not None

    # Удаляем
    db.delete_sabject_be_id(TEST_ID)

    # Проверяем что удалилось
    assert db.get_sabject(TEST_ID) is None
