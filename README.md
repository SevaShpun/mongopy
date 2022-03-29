#### MongoPy - примеры

```python
# Уникальный ID пользователя
user_id = 999

db = DataBase(user_id) # База данных

db.reg() # Регистрирует нового пользователя

db.get_list_database_names() # Получает список БД

user = db.get() # Получаем данные пользователя

user["age"] = 0 # Изменяет значение ключа и добавляет если ключ не существует
user["gold"] = 1000 # Изменяет значение ключа и добавляет если ключ не существует
user["name"] = "Kek" # Изменяет значение ключа и добавляет если ключ не существует
db.update(user) # Обновляет все введенные изменения

db.drop_user_key("gold") # Удаляет запись по ключу для указанного user_id
```
