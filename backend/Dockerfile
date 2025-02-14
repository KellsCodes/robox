FROM python:3.13.2-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app

# Create a non-root user and switch to it
RUN useradd -m appuser
USER appuser

COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000" ]