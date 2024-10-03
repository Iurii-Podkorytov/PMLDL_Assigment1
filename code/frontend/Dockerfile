FROM python:3.11.4
WORKDIR /frontend
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY main.py .
EXPOSE 8501
CMD ["streamlit", "run", "main.py"]