from main import *
from main2 import *

while True:
    print("1. User:")
    print("2. Task Manager:")

    f = input("Интихоби худро ворид кунед (1-2): ")

    if f == "1":
        while True:
            print("User:")
            print("1. Регистратсия")
            print("2. истифодабарандагон нишон дихед")
            print("3. дохил шудан")
            print("4. иазкардани рамз")
            print("5. Нест кардани истифодабаранда")
            print("6. Баргаштан ба менюи асосӣ")

            b = input("Интихоби худро ворид кунед (1-6): ")

            if b == "1":
                register()
            elif b == "2":
                users = get_users()
                for user in users:
                    print(user)
            elif b == "3":
                username = input("Номи худро ворид кунед:")
                password = input("Рамзи худро ворид кунед:")
                login(username, password)
            elif b == "4":
                username = input("Номи худро ворид кунед:")
                password = input("Рамзи худро ворид кунед:")
                change_password(username, password)
            elif b == "5":
                username = input("Номи худро ворид кунед:")
                delete(username)
            elif b == "6":
                break  

    elif f == "2":
        while True:
            print("Task Manager:")
            print("1. Илова кардани вазифа")
            print("2. Ҳама вазифаҳоро бинед")
            print("3. Нест кардани вазифа")
            print("4. баромадан")

            a = input("Интихоби худро ворид кунед (1-4): ")

            if a == "1":
                title = input("Номи вазифаро ворид кунед: ")
                description = input("Тавсифи вазифаро ворид кунед: ")
                due_date = input("Санаи анҷомёбиро ворид кунед (YYYY-MM-DD): ")
                add_task(title, description, due_date)
            elif a == "2":
                view_tasks()
            elif a == "3":
                task_id = input("ID-и вазифаро ворид кунед: ")
                delete_task(task_id)
            elif a == "4":
                print("Баромади Task Manager...")
                break  
            else:
                print("Интихоби нодуруст. Як бори дигар санҷед.")
