# Reddit Data Engineering Pipeline

This project is a comprehensive data engineering pipeline that utilizes a variety of tools and technologies to fetch, process, and analyze data from Reddit.
The pipeline is built using Python, Apache Airflow, Docker, Snowflake, and AWS services such as S3, Glue, Athena, and Redshift.

## Project Overview

The main objective of this project is to extract data from Reddit posts related to "Data Engineering," transform the data, and store it in a structured format within AWS S3. 
The stored data is then ingested into Snowflake using Snowpipe, after which it is visualized using Power BI. The project also utilizes Amazon Redshift and Athena for additional analysis and querying.

## Tech Stack

- **Python:** Core language used for data extraction and transformation scripts.
- **Apache Airflow:** Used to orchestrate the ETL process through DAGs and manage task distribution using the Celery executor.
- **Docker:** Containerizes the Airflow webserver and other services for a consistent development and production environment.
- **PostgreSQL:** Temporary storage for metadata management within Airflow.
- **Amazon S3:** Storage for raw and transformed data.
- **Snowflake:** Data warehouse where the transformed data is ingested using Snowpipe.
- **AWS Glue:** Data cataloging and ETL services to prepare data for Amazon Redshift and Athena.
- **Amazon Athena:** SQL-based data querying.
- **Amazon Redshift:** Data warehousing for complex analytics and reporting.
- **Power BI:** Data visualization tool to generate insights from the processed data.

## Workflow

1. **Data Extraction:** The project fetches data from Reddit using the Reddit API.
2. **Data Transformation:** Transformations are applied to clean and structure the data.
3. **Data Loading:** The raw and transformed data are stored in separate AWS S3 buckets.
4. **Data Ingestion:** Snowpipe automatically ingests data from the S3 bucket into Snowflake.
5. **Data Analysis:** Data is analyzed using Power BI, with additional querying via Athena and Redshift.

## Challenges & Solutions

### Hosting Airflow on Windows

Since Apache Airflow requires a Linux environment to run, several options were considered:

1. Use an AWS EC2 instance with Linux.
2. Install WSL (Windows Subsystem for Linux).
3. Use Docker to run Airflow in a Linux-based container.

**Solution:** Docker was used to containerize the Airflow environment with PostgreSQL as the metadata database and Celery as the executor.

### Data Ingestion with Snowpipe

To automate data ingestion into Snowflake, a Snowpipe was configured with an SQS queue ARN to trigger ingestion whenever new data is added to the S3 bucket.

### Data Storage in Redshift & Athena

Using AWS Glue, a data catalog was created, allowing Athena and Redshift to query the data directly from the S3 bucket.

## Setup Instructions

1. Clone the repository.
2. Build the Docker containers:
   ```bash
   docker-compose up --build

## Architecture Diagram
![RedditDataEngineering](https://github.com/user-attachments/assets/36626f2d-04f9-4d10-a4cb-d61a0b1258f5)


## For Complete working of this project refer this
https://medium.com/@abdullahk4803/reddit-data-engineering-project-0674ef75e290
