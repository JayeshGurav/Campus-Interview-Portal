# Build stage
FROM python:3.9-slim as builder

WORKDIR /app

COPY requirements.txt .
RUN pip install --user -r requirements.txt

COPY . .

# Runtime stage
FROM python:3.9-slim

WORKDIR /app

# Copy only the necessary files from the builder stage
COPY --from=builder /root/.local /root/.local
COPY --from=builder /app /app

# Ensure scripts in .local are usable
ENV PATH=/root/.local/bin:$PATH
ENV FLASK_APP=app
ENV FLASK_ENV=production

# COMMENT: Change to your preferred port
EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:create_app()"]