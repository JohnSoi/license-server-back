### Полезные команды
Инициализация миграций
```bash
flask db init
```
Создание миграций
```bash
flask db migrate -m "комментарий"
```
Применение миграций
```bash
flask db upgrade
```
Откат миграции
```bash
flask db downgrade
```
Сохранить пакеты в файл
```bash
pip freeze > requirements.txt
```
Скачать все пакеты из файла
```bash
pip install -r requirements.txt
```