FROM python:3.11-slim

WORKDIR /app

COPY requirements-frontend.txt /app/requirements-frontend.txt

ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PIP_NO_CACHE_DIR=1
ENV PIP_DEFAULT_TIMEOUT=120
ENV PIP_PROGRESS_BAR=off

RUN python -m pip install --upgrade pip setuptools wheel
RUN python -m pip install --retries 10 --timeout 120 --progress-bar off -r /app/requirements-frontend.txt

COPY frontend/ /app/

EXPOSE 8501

CMD ["streamlit", "run", "streamlit_app.py", "--server.address=0.0.0.0", "--server.port=8501"]
