<h1>Локальный python HTTP.server</h1>
<p>
<h3>Структура репозитория:</h3>
</p>
<p>

<b>/core/</b>

```
├── core
│   ├── asgi.py
│   ├── __init__.py
│   ├── routers.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── host_request
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── models.py
│   ├── services
│   │   ├── __init__.py
│   │   ├── managers.py
│   │   ├── serializers.py
│   │   └── tests.py
│   └── views.py
└── manage.py
```

В директории core - стандартный DFR проект с одним приложением 'host_request'. При отправке POST запроса на адрес http://127.0.0.1:8000/request в ответ получаем результат выполнения скрипта расположенного на локальном хосте.
</p>
<br>
<p>
<b>/local_scripts/</b>

```
├── first_script.py
├── local_server.py
├── settings.py
└── urls.py
```
В директоррии local-scripts - локальный сервер, скрипты настройки сервера, и выполняемый скрипт (first_script.py)
</p>
<ul>
  <li>first_script - скрипт выполяющий команду 'pwd' на стороне хоста</li>
  <li>local_server - python http.server (из клоробки)</li>
  <li>settings.py - скрипт с настройками сервера (адрес и порт)</li>
  <li>urls.py - скрипт со словарем описывающим пути и привязанные к ним функции</li>
</ul>
<hr>
<br>
<p>
<b>Docker-compose</b>

```
    extra_hosts:
      - "host.docker.internal:host-gateway"
```

Данная настройка для docker-compose.yml Ипользует сетевое пространство хоста и позволяет докер-контейнеру взаимодествовать с локальными портами.
<br>
<br>

```
  command: >
        /bin/bash -c "
        ...
        && chmod +x admin_add.sh && ./admin_add.sh
```

Данная настройка модифицирует права на исполнение файла admin_add.sh с последующим его выполнением. Команда распологается в модуле 'web'
</p>
<hr>
<h3>Дополнительно (опционально)</h3>
<p>
<b>admin_add.sh</b> - bash скрипт для авторегистрации админа в django. Скрипт забирает имя пользователя, почта и пароль из переменных окружения

```
  ADMIN_NAME="adminn"
  ADMIN_EMAIL="admin@mail.com"
  ADMIN_PASSWORD="123"
```

</p>
