FROM python:3

# Установите рабочую директорию
WORKDIR /code

# Скопируйте зависимости проекта в контейнер
COPY ./requirements.txt .

# Установите зависимости проекта
RUN pip install -r requirements.txt

# Скопируйте все остальные файлы проекта в контейнер
COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]