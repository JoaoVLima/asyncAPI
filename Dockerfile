FROM ubuntu:latest
LABEL authors="joao"

ENTRYPOINT ["top", "-b"]
FROM python:3.12
WORKDIR /app
COPY app /app
RUN pip install --no-cache-dir -r requirements.txt
CMD ["fastapi", "run", "app/main.py"]
