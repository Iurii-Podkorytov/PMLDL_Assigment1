FROM python:3.11.4
WORKDIR /app
COPY code/deployment/app/requirements.txt .
RUN pip install -r requirements.txt
COPY code/deployment/app/main.py .
EXPOSE 8501
CMD ["streamlit", "run", "main.py"]