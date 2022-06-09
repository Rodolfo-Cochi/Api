FROM python:3.9-alpine

WORKDIR /home/app

COPY . .

RUN pip install -r requirements.txt

CMD [ "python", "-m" , "src.main", "run", "--host=0.0.0.0"]
