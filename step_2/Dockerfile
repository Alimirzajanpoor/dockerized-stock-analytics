FROM python:3.9


WORKDIR /app


COPY performance_cal.py requirements.txt /app/


RUN pip install -r requirements.txt


CMD ["python", "performance_cal.py"]