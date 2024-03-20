# Heureka Entry Task

## Introduction

This project is a part of the Heureka Entry Task.

## Requirements

- Python 3.7+ (written in Python 3.12)
- Docker
- Colima
- Poetry as a dependency management and packaging tool.
- RabbitMQ
- PostgreSQL

## Setup

### Run FastAPI

To run the FastAPI application, use the following command:

```bash
uvicorn heureka_entry_task.app:app --reload
```
FastAPI is running on address http://127.0.0.1:8000/docs#/

### Run RabbitMQ and Database
Start Colima:

```bash
colima start
```

Run Docker Compose:
```bash
docker-compose up
```

Database is running on port: 5432
RabbitMQ management console port: 15672

### Contributors
Martina Divinová


Feel free to customize this README further as needed. Let me know if you need any more assistance!