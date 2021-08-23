FROM python:3.9.6-slim-buster

WORKDIR /app

# Install required packages
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the main code
COPY . /app

EXPOSE 5000

CMD [ "gunicorn", "-b", "0.0.0.0:5000", "app:app" ]
