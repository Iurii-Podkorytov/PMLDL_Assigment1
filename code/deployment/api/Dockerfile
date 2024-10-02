FROM python:3.11.4
WORKDIR /api
COPY code/deployment/api/requirements.txt .
RUN pip install -r requirements.txt
COPY code/deployment/api/main.py .
COPY models/model.joblib .
EXPOSE 8080
CMD ["python", "main.py"]