# Новое русское вино

Сайт магазина авторского вина "Новое русское вино".

## Запуск

Скачайте код.
Данные для публикации считываются из файла excel в рабочей папке проекта. В качестве образеца используйте wine.xlsx, находящийся в репозитории. Порядок колонок должен быть таким же, как в образце.
Укажите программе путь к файлу excel с заполненными данными. Это можно сделать двумя способами:
- задать параметр в файле переменных окружения. Для этого создайте в папке проекта папку venv, в ней создать текстовый файл с наименованием .env, в него добавить параметр EXCEL_FILE_PATH, например:
```sh
EXCEL_FILE_PATH=D:\Data files\wine.xlsx
```
- указать параметр -f в строке запуска, например:
```sh
python3 main.py -f wine.xlsx
```
Если путь указан и в файле .env, и в параметре запуска, то значение пути будет браться из параметра запуска.

В файле .env укажите дату основания предприятия в параметре FOUNDATION_YEAR, например; 
```sh
FOUNDATION_YEAR=1920
```
Если параметр не указан, то годом основания считается год, меньший текущего на 1.

Запустите сайт командой
```sh
python3 main.py [-f <Путь к файлу excel>]
```
- Перейдите на сайт по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
