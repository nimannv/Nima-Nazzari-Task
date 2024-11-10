# gRPC-based microservice



## Table of Contents
1. [Task](#task)
2. [Challenge](#challenge)
3. [Technologies](#technologies)
   - [Python gRPC Server](#python-grpc-server)
   - [FastAPI](#fastapi)
   - [InfluxDB](#influxdb)
4. [How to Run](#how-to-run)

## Task
![example tree](/README-assets/task-graph.png)
Create a gRPC server that serves the time-based electricity consumption data from `meterusage.csv`.

## Challenge
CSV is probably not an ideal data format for serving TimeSeries data. Additionally, no specific database is mentioned for this project, presenting a challenge in terms of loading data from a CSV file. To address this, I will implement additional data sources (such as InfluxDB) and design the code to support different data sources for each metric in the system.

To achieve this, I will use the **strategy design pattern** for implementing different data loaders and the **factory design pattern** for managing them in the gRPC server.

## Technologies

### Python gRPC Server
We will use Python to create the gRPC server that serves our data.

### FastAPI
[FastAPI](https://fastapi.tiangolo.com/) is a modern, fast (high-performance) web framework for building APIs with Python, based on standard Python type hints. I will use this framework for the API layer of the project. The structure and best practices are inspired by the following repository:
[FastAPI Best Practices](https://github.com/zhanymkanov/fastapi-best-practices)

### InfluxDB
[InfluxDB](https://www.influxdata.com/) is a powerful database built specifically for time series data. It will be used to store and query the electricity consumption data.

## How to Run
1. Navigate to the project directory:
   ```bash
   cd project
2. Start the services using Docker Compose:
   ```bash
   docker-compose up
3. Access the API documentation and call them at http://localhost:8000/docs.

