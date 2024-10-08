from context import *


create_database_tables()

def add_task(title,description,due_date):
    connection = open_connection()
    cur = connection.cursor()

    cur.execute(
        f""" INSERT INTO tasks (title, description, due_date)
        values(%s, %s, %s) """,(title, description, due_date))
    connection.commit()
    print("Вазифа бомуваффакият илова карда шуд.")
    close_connection(connection, cur)

def view_tasks():
    connection = open_connection()
    cur = connection.cursor()
    cur.execute("SELECT * FROM tasks ORDER BY due_date ")
    tasks = cur.fetchall()
    if not tasks:
        print("Ягон вазифа ёфт нашуд.")
    else:
        print("Задачи:")
        for i in tasks:
            print(f"ID: {i[0]}, Ном: {i[1]}, Дата: {i[3]}")
    connection.commit()
    
    close_connection(connection, cur)

def delete_task(task_id):
    connection = open_connection()
    cur = connection.cursor()
    cur.execute("DELETE FROM tasks WHERE id = %s",(task_id))
    connection.commit()
    print("Вазифа бомуваффақият нест карда шуд.")
    close_connection(connection, cur)

