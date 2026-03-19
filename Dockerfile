FROM python:3.11-slim

WORKDIR /app

COPY staff_duty/requirements-deploy.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY staff_duty/ ./staff_duty/

EXPOSE 8080

CMD ["gunicorn", "--bind", "0.0.0.0:8080", "--workers", "2", "--timeout", "60", "staff_duty.app:app"]
