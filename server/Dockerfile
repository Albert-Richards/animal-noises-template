FROM python:3.6
WORKDIR /app
COPY . .
RUN pip install flask requests
EXPOSE 5000
ENTRYPOINT ["python3", "app.py"]