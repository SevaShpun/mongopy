import pymongo


class DataBase:
    message = None

    def __init__(self, message):
        self.message = message
        self.client = pymongo.MongoClient("localhost", 27017)
        self.db = self.client.ClassicGame
        self.db_users = self.db.db_users
        self.user = self.db_users.find_one({'user_id': self.message})

    def Create(self):
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

    def Read(self, sid=0):
        if sid > 0:
            user = self.db_users.find_one({'user_id': int(sid)})
        else:
            user = self.db_users.find_one({'user_id': self.message})
        return user

    def Update(self, save_data={}):
        user={}
        for k, v in save_data.items():
            is_key = True if k in dbase.user.keys() else False
            if is_key:
                self.db_users.replace_one({"user_id": self.message}, save_data, True)
            else:
                self.db_users.update({"user_id": self.message}, {"$set": save_data})
        return self.user

    def Delete(self, del_data=""):
        return self.db_users.update({"user_id": self.message}, {"$unset": {del_data: self.user[del_data]}})


def RunWithNotice(user_id):
    client = pymongo.MongoClient("localhost", 27017)
    db = client.ClassicGame
    db_users = db.db_users

    out = ''
    if db_users.find_one({'user_id': user_id}):
        user = db_users.find_one({'user_id': user_id})
        user_id = user['user_id']
        out = f'{user_id}, уже создан!'
    else:
        base_json = {'user_id': user_id, 'name': "Dev", 'city': "Moscow"}
        result = db_users.insert_one(base_json)
        out = f'{user_id}, регистрация прошла успешно!'
    print(out)


user_id = 999
# База данных
dbase = DataBase(user_id)

# Регистрирует нового пользователя
#dbase.Create()

users = dbase.user
# Изменяет ключ:значение и добавляет, если ключ не существует
users["ark"] = "gqq2"
users["age"] = 21
users["don"] = "q2"
users["tss"] = "yes"
dbase.Update(users)

# Удаляет запись по ключу для указанного user_id
dbase.Delete("ark")
