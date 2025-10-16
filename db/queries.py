CREATE_TABLE = """
    CREATE TABLE IF NOT EXISTS tasks(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task TEXT NOT NULL
    )
"""

INSERT_task = 'INSERT INTO tasks (task) VALUES (?)'

SELECT_TASK = 'SELECT ID, task FROM tasks'

UPDATE_TASK = 'UPDATE tasks SET task = ? WHERE id = ?'

DELETE_TASK = 'DELETE FROM tasks WHERE id = ?'
