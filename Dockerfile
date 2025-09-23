# Rasm: Python 3.11
FROM python:3.11-slim

# Ishchi papkani yaratish
WORKDIR /app

# Dependensiyalarni ko‘chirib olish
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Loyihani ko‘chirish
COPY . .

# Statik fayllarni yig‘ish
RUN python manage.py collectstatic --noinput

# Serverni ishga tushirish
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]
