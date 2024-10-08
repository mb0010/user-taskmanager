from context2 import *

create_database_tables()

def register():
    connection = open_connection()
    cur = connection.cursor()
    cur.execute(
        f""" insert into users(username, password, first_name, last_name, email)
        values(
            '{input("username: ")}',
            '{input("password: ")}',
            '{input("first_name: ")}',
            '{input("last_name: ")}',
            '{input("email: ")}'
        ) """
    )
    connection.commit()
    print("Шумо бомуваффакият дохил шудед.")
    close_connection(connection, cur)


def get_users():
    conn = open_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users ORDER BY email ")
    users = cur.fetchall()
    if not users:
        print("Ягон одам ёфт нашуд ёфт нашуд.")
    else:
        print("Users:")
        for i in users:
            print(f"username: {i[0]}, first_name: {i[2]}, last_name: {i[3]}, email: {i[4]}")
    close_connection(conn,cur)
    


def login(username, password):
    conn = open_connection()
    cur = conn.cursor()
    cur.execute(f"select * from users where username = '{username}' and password = '{password}'")
    user = cur.fetchone()
    print("Шумо дохил шудед")
    close_connection(conn,cur)
    return user



def change_password(username,password):
    conn = open_connection()
    cur = conn.cursor()
    cur.execute(f"update users set password='{input('Enter new password: ')}'  where username = '{username}' and password = '{password}'")
    conn.commit()
    print("Рамзи шумо иваз шуд")
    close_connection(conn,cur)




def delete(username):
    conn = open_connection()
    cur = conn.cursor()
    a = input("do you want delete your acaunt: ")
    if a == "Yes":
        cur.execute(f"delete from users where username = '{username}'")
    else :
        pass
    conn.commit()
    close_connection(conn,cur)



