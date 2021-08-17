FROM python:3.9-slim-buster

WORKDIR /app

# Install required packages
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Copy the main code
COPY . /app

# Configure environement variables
ENV FLASK_ENV=development

CMD [ "flask", "run", "--host", "0.0.0.0", "--port", "5000" ]
