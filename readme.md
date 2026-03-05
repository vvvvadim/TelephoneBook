# TelephoneBook 📞

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)](https://developer.mozilla.org/ru/docs/Web/JavaScript)

Веб-приложение для отображения корпоративного телефонного справочника с возможностью инициации звонков по клику. 
Проект состоит из бэкенда на **FastAPI** и динамического веб-интерфейса.

## ✨ Возможности

*   🏢 **Иерархическая структура**: Город → Отдел → Сотрудник
*   📍 **Адреса офисов**: Отображение адреса для каждого города (виден всегда, даже при свернутом городе)
*   📞 **Быстрые звонки**: Клик на любой номер телефона инициирует POST-запрос к API
*   🔍 **Поиск**: Фильтрация сотрудников по Ф.И.О. с подсветкой результатов
*   📄 **Экспорт в PDF**: Сохранение справочника в формате PDF с красивым форматированием
*   🔐 **Сохранение номера менеджера**: Внутренний номер сохраняется в localStorage браузера
*   🐳 **Docker-ready**: Готов к запуску через Docker Compose

## 🚀 Быстрый старт

### Предварительные требования

*   [Docker](https://www.docker.com/) и [Docker Compose](https://docs.docker.com/compose/) (для запуска в контейнерах)
*   Или Python 3.9+ и зависимости для запуска без Docker

### Запуск с использованием Docker (рекомендуемый способ)

1.  **Клонируйте репозиторий:**
    ```bash
    git clone https://github.com/vvvvadim/TelephoneBook.git
    cd TelephoneBook

    Запустите контейнеры:
    bash

    docker-compose up -d

    Откройте приложение:
    Перейдите в браузере по адресу http://localhost:8000

Запуск без Docker

    Клонируйте репозиторий:
    bash

    git clone https://github.com/vvvvadim/TelephoneBook.git
    cd TelephoneBook

    Создайте виртуальное окружение и установите зависимости:
    bash

    python -m venv venv
    source venv/bin/activate  # для Linux/Mac
    # или
    venv\Scripts\activate  # для Windows

    pip install fastapi uvicorn jinja2

    Запустите сервер:
    bash

    uvicorn api.main:app --reload --host 0.0.0.0 --port 8000

    Откройте приложение:
    Перейдите по адресу http://localhost:8000

📁 Структура проекта
text

TelephoneBook/
├── api/                    # Бэкенд на FastAPI
│   ├── __init__.py
│   ├── main.py            # Точка входа FastAPI
│   └── routers/           # Роуты API
│       └── calls.py       # Обработка звонков
├── book/                   # Фронтенд и статические файлы
│   ├── index.html          # Основная HTML-страница
│   └── telephonebook.json  # Данные справочника
├── .gitignore
├── docker-compose.yaml     # Конфигурация Docker Compose
└── README.md               # Документация проекта

🗂️ Формат данных (book/telephonebook.json)

Данные справочника хранятся в JSON-файле со следующей структурой:
json

{
  "Москва": {
    "icon": "🏢",
    "address": "ул. Ленина, д. 1, БЦ 'Москва-Сити', офис 501",
    "departments": {
      "Отдел продаж": {
        "icon": "💰",
        "employees": [
          {
            "fio": "Иванов Иван Иванович",
            "position": "Руководитель отдела продаж",
            "phones": [
              { "number": "1101", "type": "добавочный" },
              { "number": "+7 (495) 123-45-67", "type": "городской" },
              { "number": "+7 (903) 111-22-33", "type": "мобильный" }
            ],
            "email": "i.ivanov@company.ru"
          }
        ]
      }
    }
  }
}

🛠️ Использование
1. Ввод номера менеджера

При первом входе введите ваш 4-значный внутренний номер — он сохранится в браузере и будет использоваться для всех звонков.
2. Навигация по справочнику

    Клик по заголовку города сворачивает/разворачивает все отделы в этом городе

    Клик по заголовку отдела сворачивает/разворачивает список сотрудников

    Адрес офиса всегда виден, независимо от состояния сворачивания

3. Поиск сотрудников

Используйте строку поиска для фильтрации сотрудников по Ф.И.О. Найденные совпадения подсвечиваются желтым цветом.
4. Совершение звонка

Нажмите на любой номер телефона сотрудника. Будет отправлен POST-запрос на:
text

/api/calls?manager={ваш_номер}&client_number={номер_сотрудника}

5. Экспорт в PDF

Нажмите кнопку «Экспорт в PDF» в правом верхнем углу для сохранения всего справочника в формате PDF.
🔧 API Endpoints
Метод	Endpoint	Описание
GET	/	Главная страница справочника
POST	/api/calls?manager=XXXX&client_number=YYYY	Инициация звонка
🤝 Вклад в проект

Если вы хотите сообщить об ошибке или предложить улучшение:

    Создайте Issue в репозитории на GitHub

    Опишите проблему или идею

    Для Pull Request'ов:

        Сделайте fork репозитория

        Создайте ветку для ваших изменений

        Отправьте Pull Request с описанием изменений

🐳 Docker

Проект полностью готов к запуску в Docker. Файл docker-compose.yaml содержит конфигурацию для сервиса:
yaml

version: '3.8'

services:
  web:
    build: .
    ports:
      - "8000:8000"
    volumes:
      - ./book:/app/book
    restart: unless-stopped

📄 Лицензия

Проект распространяется под лицензией MIT. Подробнее см. в файле LICENSE.
👨‍💻 Автор

vvvvadim - GitHub Profile

⭐ Если проект оказался полезным, поставьте звезду на GitHub! ⭐

Сделано с ❤️ для удобства работы с корпоративными контактами.