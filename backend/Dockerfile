FROM python:3.12-slim
WORKDIR /app
RUN useradd -U appuser
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN chown -R appuser:appuser /app
USER appuser
CMD ["python", "app.py"]
