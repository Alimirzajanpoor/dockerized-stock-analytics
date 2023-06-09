FROM python:3.9


WORKDIR /app


COPY updater_price.py requirements.txt /app/


RUN pip install -r requirements.txt


CMD ["python", "updater_price.py"]
