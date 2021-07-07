FROM python:3.6
WORKDIR /app
COPY . .
RUN pip install flask requests flask_sqlalchemy pymysql
EXPOSE 5000
ENTRYPOINT ["python3", "app.py"]