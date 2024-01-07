# Используем официальный образ Python для Windows
FROM python:3.10

# Устанавливаем переменную окружения для предотвращения вывода веб-приложения в режиме буферизации
ENV PYTHONUNBUFFERED 1\
    BOT_TOKEN=6006947703:AAFiIBqbYWhmZUl6l1crqb3ZbQI4CpiXkoU

# Создаем и переключаемся в рабочую директорию /app
WORKDIR /app

# Копируем файл requirements.txt в рабочую директорию
COPY requirements.txt /app/

# Устанавливаем зависимости
RUN python -m venv venv
RUN . venv/bin/activate && pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Копируем все файлы из текущего контекста сборки в рабочую директорию
COPY . /app/

VOLUME ["/app/data"]
# Экспонируем порт 8000 (или другой, если ваше приложение использует другой порт)
EXPOSE 3000

# Команда для запуска приложения
CMD ["python", "bot.py"]
