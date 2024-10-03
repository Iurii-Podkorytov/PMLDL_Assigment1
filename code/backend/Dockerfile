FROM python:3.11.4
WORKDIR /backend
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY main.py .
COPY models/model.joblib ./models/
EXPOSE 8080
CMD ["python", "main.py"]