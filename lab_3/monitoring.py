import requests
import json
import logging
import time
import threading

logging.basicConfig(
    filename="server.log",
    filemode='a',
    level=logging.INFO,
    format='{levelname} {asctime} {name} : {message}',
    style='{'
)
log = logging.getLogger(__name__)

def main(url):
    try:
        r = requests.get(url)
        data = json.loads(r.content)
        logging.info("Сервер доступний. Час на сервері: %s", data['date'])
        logging.info("Запитувана сторінка: : %s", data['current_page'])
        logging.info("Відповідь сервера місти наступні поля:")
        for key in data.keys():
            logging.info("Ключ: %s, Значення: %s", key, data[key])
        print("Запуск успішний")
    except:
        print("Помилка підключення до сервера")
        logging.error("Не під'єднано до сервера")
        logging.warning("Не під'єднано до сервера")


if __name__ == '__main__':
    while True:
        main("http://localhost:8000/health")
        time.sleep(60)