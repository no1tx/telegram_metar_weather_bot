# telegram_metar_weather_bot
Telegram weather bot, which gets data from http://metartaf.ru in JSON, decode it and send in response. Requires a Python 3, metar, pytelegrambotapi and requests packages.
You can also build Docker image to run bot in Docker environment.
To do that:

>git clone https://github.com/no1tx/telegram_metar_weather_bot

>cd telegram_metar_weather_bot

>docker build -t tgmetarbot .

>docker run tgmetarbot
