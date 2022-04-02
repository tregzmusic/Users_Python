#список пользователей
users = ["user1", "user2", "user3"]
name_user = input("Введите имя пользователя: ")

#пользователь должен user1
if users[0] == name_user:
    password = input("Введите пароль: ")
    print("Вы успешно зашли в систему")
else:
    print("Error")