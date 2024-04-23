# RealTime-Streaming-FinanceData-Pipeline

This project sets up a robust, distributed data processing pipeline using Apache Airflow for orchestration, Apache Kafka for stream processing, Apache Spark for data analysis, and Apache Cassandra for data storage. The system is designed to ingest real-time financial data from the Finnhub API, process it, and persist it for analytics purposes.

## System Architecture

- **Apache Airflow**: Orchestrates the data pipeline workflows.
- **Apache Kafka**: Handles the streaming data input and output.
- **Apache Spark**: Processes the data and performs analytics.
- **Apache Cassandra**: Stores the processed data.
- **Docker**: Containers for each component ensure isolation and scalability.

## Directory Structure
```
finhub-data-pipeline/
│
├── docker-compose.yml
│
├── kafka/
│   └── kafka-init.sh
│
├── spark/
│   ├── Dockerfile
│   └── spark-job.py
│
├── airflow/
│   ├── Dockerfile
│   ├── dags/
│   │   └── finhub_ingest_dag.py
│   └── plugins/
│
└── cassandra/
    ├── init.cql
    └── Dockerfile
```
## Setup

To get started, make sure Docker and Docker Compose are installed on your system.

1. Build the custom Docker images:
   ```
   docker build -t my-spark-job ./spark
   docker build -t my-airflow ./airflow
   docker build -t my-cassandra ./cassandra
   ```
2. Start the services with Docker Compose:
   ```
   docker-compose up -d
   ```
3. Check the logs to ensure all services are running correctly:
   ```
   docker-compose logs
   ```

## Usage

Once the services are up and running:

- Access the Airflow web interface at `http://localhost:8081` to monitor and trigger DAG runs.
- Access the Spark Master UI at `http://localhost:8080` to monitor Spark jobs.
- Use CQLSH to interact with Cassandra at `cassandra:9042`.

## Customization

- Modify the DAGs in the `airflow/dags/` directory to orchest

rate different workflows.
- Place custom Spark job scripts in `spark/` for data processing tasks.
- Extend functionality with custom Airflow plugins by adding them to `airflow/plugins/`.
- Adjust the Cassandra schema in `cassandra/init.cql` as per your data model requirements.

## Contributing

Contributions to improve the data pipeline or extend its functionalities are welcome. Please adhere to this project's `code of conduct` while contributing.

## License

[Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0)

## Contact

- For any inquiries or to report issues, please open an issue on the repository's issue tracker.

## Acknowledgements

- Thanks to Finnhub for providing the financial data API.
- This project utilizes several open-source technologies listed in the `System Architecture` section; all rights and acknowledgments for these tools go to their respective owners.

```
