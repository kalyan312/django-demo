FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN pip install --no-cache-dir --upgrade pip

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

# We will run manage.py from the git-synced folder at runtime
CMD ["sh", "-lc", "cd /app/repo && python manage.py runserver 0.0.0.0:8000"]
