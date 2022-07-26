FROM python:latest

WORKDIR /usr/src/myapp

COPY ./src/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src .

EXPOSE 8000

WORKDIR /usr/src/myapp/src

CMD [ "uvicorn", "main:app", "--reload", "--host",  "0.0.0.0", "--port", "80" ]   
