# Dockerfile

FROM python:3.11.4

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . code
WORKDIR /code

EXPOSE 8000

ENTRYPOINT ["python", "backend/manage.py"]
CMD ["runserver", "0.0.0.0:8000"]
