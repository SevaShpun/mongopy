import pymongo
from settings import *

class DB:
    message = None

    def __init__(self, message):
        self.message = message
        self.client = pymongo.MongoClient(f'{cfg_url}@{cfg_server}/{cfg_db}?{cfg_options}')
        self.db = self.client.get_database('gamedb')
        self.db_users = self.db.db_users
        self.user = self.db_users.find_one({'user_id': self.message})

    def get_list_database_names(self):
        """Отображает список баз данных
        >>> db = DB(user_id)
        >>> db.get_list_database_names() -> list
        """
        print(self.client.list_database_names())

    def reg(self):
        """Регистрирует пользователя
        >>> db = DB(user_id)
        >>> db.reg()
        """
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
        """Считывает данные пользователя
        >>> db = DB(user_id)
        >>> user = db.get() -> dict
        >>> print(user["name"])
        """
        if user_id:
            user = self.db_users.find_one({'user_id': int(user_id)})
        else:
            user = self.db_users.find_one({'user_id': self.message})
        return dict(user)

    def update(self, user:dict=None):
        """Обновляет данные пользователя
        >>> db = DB(user_id)
        >>> user = db.get()
        >>> user["city"] = "Moscow"
        >>> db.update(user)
        """
        return self.db_users.update_one({"user_id": self.message}, {"$set": user})

    def drop_user_key(self, key_name:None):
        """Пример 1
        >>> drop_user_key("name")
        ... удаляет ключ name
        Пример 2
        >>> drop_user_key(["name", "age", "city"])
        ... удаляет указанные ключи из списка
        Пример 3
        ... если у вас такой словарь, то...
        {
            "res": {
                "gold": 100,
                "wood": 500,
                "stone": 800,
                "iron": 300,
                "food": 500
            }
        }
        >>> drop_user_key({"res": ["gold", "stone", "iron"]})
        ... удаляет указанные ключи из списка словаря res
        ... для удаления самого ключа словаря (Пример 1)
        """
        
        if isinstance(key_name, str):
            if self.get().get(key_name, None):
                return self.db_users.update_one({"user_id": self.message}, {"$unset": {key_name: self.get()[key_name]}})
        
        if isinstance(key_name, list):
            for k_name in key_name:
                if self.get().get(k_name, None):
                    return self.db_users.update_one({"user_id": self.message}, {"$unset": {k_name: self.get()[k_name]}})

        if isinstance(key_name, dict):
            user = self.get()
            for root_key, root_value in key_name.items():
                for k_name in root_value:
                    if self.get().get(root_key, None).get(k_name, None):
                        del(user[root_key][k_name])
                return self.db_users.update_one({"user_id": self.message}, {"$set": {root_key: user[root_key]}})
