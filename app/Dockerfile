FROM python:3.11-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --target=/app/dependencies -r requirements.txt

FROM gcr.io/distroless/python3-debian12:latest
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY --from=builder /app/dependencies /app/dependencies
COPY . /app
ENV PYTHONPATH=/app/dependencies
CMD ["/app/app.py"]