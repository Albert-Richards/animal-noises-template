# Dockerfile for a Python App
FROM python:3.6
WORKDIR /app
COPY . .
RUN pip install flask
EXPOSE 5000
ENTRYPOINT ["python3", "app.py"]