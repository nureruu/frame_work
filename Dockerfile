
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .


RUN pip install --upgrade pip && pip install -r requirements.txt


COPY . .
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

CMD ["gunicorn", "shop_api.wsgi:application", "--bind", "0.0.0.0:8000"]
