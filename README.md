
# gRPC-Based Microservice

## Table of Contents
1. [Task](#task)
2. [Challenges](#challenges)
   - [Data Source](#data-source)
   - [Data Cleaning](#data-cleaning)
3. [Future Enhancements](#future-enhancements)
4. [Technologies](#technologies)
   - [Python gRPC Server](#python-grpc-server)
   - [FastAPI](#fastapi)
   - [Typer](#typer)
   - [InfluxDB](#influxdb)
5. [Project Structure](#project-structure)
   - [Directory Structure](#directory-structure)
6. [How to Run](#how-to-run)
   - [Using Docker](#using-docker)
   - [Without Docker](#without-docker)

## Task
![Task Overview](./README-assets/task-graph.png)  
Create a gRPC server that serves time-based electricity consumption data from `meterusage.csv`.

## Challenges

### Data Source
CSV may not be the most efficient format for serving time-series data. Additionally, no specific database has been designated for this project, presenting a challenge in terms of loading data. To address this, multiple data sources (such as InfluxDB) will be integrated. The code will be designed to be flexible, allowing support for different data sources for each metric.

To implement this, the **Strategy Design Pattern** will handle different data loaders and the **Factory Design Pattern** will manage these loaders within the gRPC server.

### Data Cleaning
A row in the CSV file contains a NaN value. For now, it is deleted to ensure data integrity.

## Future Enhancements
1. **Additional Data Loaders:** Integrate other data loaders (e.g., TimescaleDB) for testing and comparing different time-series databases. This will help determine the best fit for the project.
2. **Data Seeders:** Develop data seeders to transform and load data into various data stores (InfluxDB, TimescaleDB, etc.), ensuring data compatibility across different databases.
3. **Streaming:** Introduce gRPC streaming to optimize data loading, providing real-time data to clients instead of loading all data at once as the dataset grows.

## Technologies

### Python gRPC Server
Python will be used to create the gRPC server that serves the data.

### FastAPI
[FastAPI](https://fastapi.tiangolo.com/) is a modern, fast (high-performance) web framework for building APIs with Python. It will be used to build the API layer of the project, following best practices outlined in the [FastAPI Best Practices](https://github.com/zhanymkanov/fastapi-best-practices) repository.

### Typer
[Typer](https://typer.tiangolo.com/) is a library for building command-line interface (CLI) applications. It will manage project commands, such as running the project, executing tests, and other administrative tasks.

### InfluxDB
[InfluxDB](https://www.influxdata.com/) is a database designed for storing and querying time-series data. It will store electricity consumption data.

## Project Structure

### Directory Structure
\`\`\`
project/
├── docker-compose.yml
├── rest_api_gateway/      # FastAPI application
├── grpc_server/           # gRPC server data provider
├── influxdb/              # Timeseries database
└── .env                   # Environment variables for Docker Compose
\`\`\`

### `grpc_server` and `rest_api_gateway`
Both `grpc_server` and `rest_api_gateway` have the following structure:
```
.../
├── requirements.txt
├── .env                   # Env variables for internal service configs
├── Dockerfile
└── app/                   # Application that executes in the container
    ├── manage.py          # CLI to work with the application
    └── src/               # Application source code
        └── ...
```

Everything starts from **manage.py**! `manage.py` uses Typer and acts as an interface to work with the application.

You can see available commands by executing this command in the **/app** directory:
```
python manage.py --help
```

## How to Run

### Using Docker

1. Navigate to the project directory:
   \`\`\`
   cd project
   \`\`\`
2. Create `.env` files. You can do this easily by using `.env.sample` files. Make a copy of them or rename them:
   - `project/.env.sample`
   - `project/grpc_server/.env.sample`
   - `project/rest_api_gateway/.env.sample`
3. Start the services using Docker Compose:
   \`\`\`
   docker-compose up
   \`\`\`
4. Access the API documentation at [http://localhost:8000/docs](http://localhost:8000/docs).

### Without Docker

1. Run `grpc_server`:
   \`\`\`
   cd project/grpc_server
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   python manage.py runserver 50051
   \`\`\`

2. Run `rest_api_gateway`:
   \`\`\`
   cd project/rest_api_gateway
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   python manage.py runserver 8000
   \`\`\`

3. Access the API documentation at [http://localhost:8000/docs](http://localhost:8000/docs).

Note: InfluxDB can only be used via Docker.

