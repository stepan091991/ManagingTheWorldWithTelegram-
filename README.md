# Managing the world with telegram
Внимание! Бот работает только на сервере майнкрафт
с поддержкой Rcon.

С помощью этой программы вы сможете управлять
миром или игроком в майнкрафт с помощью отправки команд в telegram бота.
Все объяснения настроек находятся ниже.

Для начала настройки, перед запуском программы
откройте скрипт <script.py> и вписывайте значения в строки
по списку ниже.

| Настройка | Объяснение  |
| :---:   | :-: |
| Token | Токен бота в телеграме.|
| Sleep_time | Задержка между сообщениями |
| Start_message | Сообщение(я) при каманде /start.|
| None_command_message | Сообщение(я) при отсутствии команды.|
| Debug_messages(True or False) | Отладка в консоль.|
| Server_IP | Ip сервера.|
| Auto_run_server(True or False) | Автоматический запуск сервера при запуске скрипта. |
| Part_to_server_bat | Путь к файлу запуска сервера(Работает при включеном Auto_run_server). |
| Server_run_time | Время(в секундах), уходящее на запуск сервера(работает при включеном Auto_run_server). |
| Stop_server_message | Сообщение для отключения сервера и программы. |
| Rcon_password | Пароль от Rcon. |

Для добавления команд в бота откройте файл.
Там будет содержаться шаблон. Добавляете по нему команды.

После запуска программы у вас откроется консоль(и сервер, если включён Auto_run_server).
Пожалуйста!Если заметите баг или будите изменять скрипт, то пишите на почту mana_the_world_with_tel_help@mail.ru
