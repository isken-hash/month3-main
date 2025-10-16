import sqlite3
from db import queries
from config import path_db


def init_db():
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.CREATE_TABLE_TASKS)
    print("база данных подлкючена")
    conn.commit()
    conn.close()

def get_task(task):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.SELECT_TASK)
    tasks = cursor.fetchall()
    conn.close()
    return tasks
