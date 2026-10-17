"""
Задача 5. LEFT JOIN і підрахунок без розмноження
Варіант 15: Фітнес-клуб (набір 3)
"""

VARIANT = 15


def query() -> str:
    return """
    SELECT
        h.name,
        count(DISTINCT w.id) AS items,
        count(b.id) AS links,
        coalesce(sum(b.places), 0) AS total_qty
    FROM hall h
    LEFT JOIN workout w ON w.hall_id = h.id
    LEFT JOIN booking b ON b.workout_id = w.id
    GROUP BY h.id, h.name
    ORDER BY links DESC, h.id ASC;
    """