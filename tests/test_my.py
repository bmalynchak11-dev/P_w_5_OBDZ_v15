from conftest import load
from pgutil import Db
from schemas import SCHEMAS


def test_my_case():
    db = Db()
    try:
        # Завантажуємо набір даних 3 (фітнес-клуб)
        db.run(SCHEMAS[3])
        # Додаємо новий порожній зал без тренувань для перевірки збереження рядків без пар
        db.run("INSERT INTO hall (id, name, location) VALUES (999, 'Тестовий новий зал', 'Сектор Z');")
        rows = db.rows(load(5).query())
        # Переконуємося, що новий зал потрапив у результат із нульовими показниками
        hall_names = [r[0] for r in rows]
        assert "Тестовий новий зал" in hall_names
        
        # Знаходимо доданий зал і перевіряємо нулі
        test_hall = next(r for r in rows if r[0] == "Тестовий новий зал")
        assert test_hall[1] == 0  # items
        assert test_hall[2] == 0  # links
        assert test_hall[3] == 0  # total_qty
    finally:
        db.close()