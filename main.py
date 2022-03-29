from database import DB

# Уникальный ID пользователя
user_id = 999

# База данных
db = DB(user_id)

# Регистрирует нового пользователя
# db.reg()

# Получает список БД
# db.get_list_database_names()

# Получаем данные пользователя
user = db.get()
print(user)
# Изменяет значение
user["name"] = "Kek"
user["age"] = 0
user["res"] = {
    "gold": 100,
    "wood": 500,
    "stone": 800,
    "iron": 300,
    "food": 500
}
# db.update(user)

# Удаляет запись по ключу для указанного user_id
# db.drop_user_key("res")
# db.drop_user_key(["age", "name"])
# db.drop_user_key({"res": ["gold", "stone", "iron"]})
