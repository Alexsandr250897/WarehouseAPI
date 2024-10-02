FROM python:3.12
WORKDIR /app
RUN pip install poetry
COPY pyproject.toml poetry.lock ./
RUN poetry export -f requirements.txt | pip install -r /dev/stdin --no-deps
EXPOSE 8000
COPY . ./
CMD ["uvicorn", "warehouse.main:app", "--host", "0.0.0.0", "--port", "8000"]