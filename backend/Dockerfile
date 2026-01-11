FROM python:3.11-slim
WORKDIR /app

COPY requirements-backend.txt /app/requirements-backend.txt

ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PIP_NO_CACHE_DIR=1
ENV PIP_DEFAULT_TIMEOUT=120
ENV PIP_PROGRESS_BAR=off

RUN python -m pip install --upgrade pip setuptools wheel
RUN python -m pip install --retries 10 --timeout 120 --progress-bar off -r /app/requirements-backend.txt

COPY backend/ /app/

EXPOSE 8000

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
