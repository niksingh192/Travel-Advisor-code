FROM python:3.8-slim
WORKDIR /app
COPY travel-advisor.py /app/travel-advisor.py
COPY REST-api.py /app/REST-api.py
COPY requirements.txt /app/requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt
EXPOSE 8080
CMD ["python3", "REST-api.py"]
