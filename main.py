import pymongo
import json

def settings():
    with open("settings.json", "r", encoding="utf-8") as f:
        return dict(json.loads(f.read()))

CFG = settings()

cfg_url = CFG.get("url")
cfg_server = f'{CFG.get("servers")[0]},{CFG.get("servers")[1]},{CFG.get("servers")[2]}'
cfg_db = CFG.get("db")
cfg_options = CFG.get("options")

class DataBase:
    message = None

    def __init__(self, message):
        self.message = message
        self.client = pymongo.MongoClient(f'{cfg_url}@{cfg_server}/{cfg_db}?{cfg_options}')
        self.db = self.client.get_database('gamedb')
        self.db_users = self.db.db_users
        self.user = self.db_users.find_one({'user_id': self.message})

    def get_list_database_names(self):
        print(self.client.list_database_names())

    def reg(self):
        out = ""
        if self.db_users.find_one({'user_id': self.message}):
            user = self.db_users.find_one({'user_id': self.message})
            user_id = user['user_id']
            out = f"{user_id}, уже есть!"
        else:
            base_json = {'user_id': self.message, 'name': "Dev", 'city': "SPB"}
            result = self.db_users.insert_one(base_json)
            out = f"{self.message}, регистрация прошла успешно!"
        return out

    def get(self, user_id:int=None):
        if user_id:
            user = self.db_users.find_one({'user_id': int(user_id)})
        else:
            user = self.db_users.find_one({'user_id': self.message})
        return dict(user)

    def update(self, user:dict=None):
        return self.db_users.update_one({"user_id": self.message}, {"$set": user})

    def drop_user_key(self, key_name:str):
        if self.get().get(key_name, None):
            return self.db_users.update_one({"user_id": self.message}, {"$unset": {key_name: self.get()[key_name]}})


# Уникальный ID пользователя
user_id = 999

db = DataBase(user_id) # База данных

# db.reg() # Регистрирует нового пользователя

# db.get_list_database_names() # Получает список БД

# user = db.get() # Получаем данные пользователя

# user["age"] = 0 # Изменяет значение ключа и добавляет если ключ не существует
# user["gold"] = 1000 # Изменяет значение ключа и добавляет если ключ не существует
# user["name"] = "Kek" # Изменяет значение ключа и добавляет если ключ не существует
# db.update() # Обновляет все введенные изменения
# print(db.update(user))
# print(db.drop_user_key("gold")) # Удаляет запись по ключу для указанного user_id
