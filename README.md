# ***CRUD-приложение на ️[FastAPI](https://github.com/fastapi/fastapi)***
##
## Запуск на пк💻
### **1. Клонирование репозитория**
> git clone https://github.com/MaxWorkIT/Very-Simple-Web-App.git
### **2. Установка всех зависимостей**
> cd technical_additions
> ######
> pip install '-r' requirements.txt
#### *или*
> pip install fastapi[all]
### **3. Запуск через uvicorn**
> uvicorn main_files.main:app
### **4. Переход по [ссылке](http://127.0.0.1:8000/docs)**
#
## Эксплуатация📺
### Есть два блока:
```sport_motivation```🏋🏻 и ```study_motivation```👨🏻‍💻 *(мотивация для спорта и для учёбы соответственно)*
#### ***В каждом из которых вы можете производить некоторые действия с данными***
*(в основном с фразами и цитатами для мотивации)*
###
### В каждом блоке есть различные HTTP-запросы
> GET ➜ получение данных
######
> POST ➜ добавление данных
######
> PUT и PATCH ➜ изменение данных
######
> DELETE ➜ удаление данных