#### MongoPy - примеры

## Регистрация пользователя
```python
from database import DB

# Уникальный ID пользователя
user_id = 999

# База данных
db = DB(user_id)

# Регистрирует нового пользователя
db.reg()
```

## Считываем данные пользователя
```python
from database import DB

# Уникальный ID пользователя
user_id = 999

# База данных
db = DB(user_id)

# Получаем данные пользователя
user = db.get()
print(user["name"])
```

## Обновление данных пользователя
```python
from database import DB

# Уникальный ID пользователя
user_id = 999

# База данных
db = DB(user_id)

# Получаем данные пользователя
user = db.get()

user["name"] = "Alex"
user["res"] = {
    "gold": 100,
    "wood": 500,
    "stone": 800,
    "iron": 300,
    "food": 500
}
# Если ключ не существует, то добавляется с данными
# Обновляем/Добавляем данные
db.update(user)
```

## Удаление данных пользователя
```python
from database import DB

# Уникальный ID пользователя
user_id = 999

# База данных
db = DB(user_id)

# Удаляет ключ 'name' (строка)
db.drop_user_key("name")

# Удаляет ключи из списка (список)
db.drop_user_key(["age", "city"])

# Удаляет ключи из соваря 'res' (словарь)
db.drop_user_key({"res": ["gold", "stone", "iron"]})
```
