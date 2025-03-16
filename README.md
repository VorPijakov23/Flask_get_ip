# Flask get ip

# ARCHIVED

Flask get ip - Простой Flask сервер с бесплатным рандомным доменом, собирающий данные подключившихся


## Описание

При запуске сервера, запускается два процесса:
- get_domain
- start_server

get-domain выполняет команду `ssh -R 80:localhost:{port} serveo.net` где `port` это порт на котором работает сервер (поменять можно в apps/config.py).

start_server запускает flask сервер на том же порту как и get-domain. На главной и единственной страннице он показывает и сохраняет все данные пользователя которые может получить.

## Установка

### Клонирование репозитория, и переход в каталог

```bash
git clone https://github.com/VorPijakov23/Flask_get_ip.git

cd Flask_get_ip/
```
### Запуск скрипта для подготовки к работе

#### В Mac/linux
```bash
bash install_scripts/install.sh
```
#### В Windows
```bash
install_scripts/install.bat
```

**Flask get ip** готов к работе!

## Запуск и использование
### Запуск
```bash
python3 main.py
```
### Использование
#### Сервер запускается на заданном вами порту(По умолчанию 35123). Далее запускается ssh запрос к сервису [serveo](https://serveo.net/).
Данный сервис может временно не работать по неизвестным мне причинам, поэтому стоит учитывать что в терминале может не появится сгенерированный URL:
```bash
$ python3 main.py
 * Serving Flask app 'apps.server'
 * Debug mode: off
ssh: connect to host serveo.net port 22: Connection refused
```
#### Если сервис всетаки доступен, то вы должны увидеть URL в терминале, перейдя на который, вы увидите свои данные, полученные сервером.
В корневой папке проекта есть скрипт shorten_url.py, его можно использовать для сокращения вашего(И не только) URL с помощью сервиса [click.ru](https://clck.ru/).

#### Остановить программу можно 3 раза нажав ^C (Знаю что костыль, потом буду исправлять)


#### Все данные сохраняются в файлы ips и ips_info

- **ips** - Cодержит все ip подключившиеся за всё время(без повторов).

- **ips_info** - Cодержит подробную информацию о пользователе (тоже без повторов). При подключении ip, которого нет в файле ips, в ips_info записывается подробная информация. Все последующие подключения клиента записыпаются только ip адресом.


## История версий

v1.1.0 - Первая версия представляет из себя начальную (если честно, не совсем проработанную) версию

v1.2.0 - 
 + Добавлен пункт ip_info в json файл
 + Добавление времени захода по url в лог файл
 + Код был переписан на асинхронный
 + Изменены комментарии
 + Немного исправлен синтаксис
 + Добавлен код для Arduino (Это уже для меня)
 + Удалён файл с байт кодом (\_\_pycache__)
 + Убраны лишние пункты в json (args, form, files)
 + Добавлены пункты (debug, time_temp, url_ip_info) в config.py

1.2.1 -
 + Исправлен баг в файле apps/server.py

1.2.2 - 
 + Добавлены установочные скрипты для Windows и для Unix-подобных систем

Last v2.0.0 - 
 + Код переписан под ООП

TODO v2.0.1 - Переписать архитектуру программы, пофиксить баги
