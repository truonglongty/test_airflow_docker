# # Use the official Apache Airflow image as the base image
# FROM apache/airflow:latest

# # Install any additional dependencies required for your DAG
# # For example, if your DAG requires psycopg2 to interact with PostgreSQL
# RUN pip install psycopg2-binary

# # Set the working directory to the Airflow DAGs folder
# WORKDIR /usr/local/airflow/dags

# # Copy your DAG file into the container
# COPY dags/tips_dag.py .

# # Initialize the Airflow database
# RUN airflow db init

# # Define the command to execute when the container starts
# CMD ["airflow", "dags", "unpause", "tips_dag"]


# Use the official Apache Airflow image as the base image
FROM apache/airflow:latest

# Install any additional dependencies required for your DAG
# For example, if your DAG requires psycopg2 to interact with PostgreSQL
RUN pip install psycopg2-binary

# Set the working directory to the Airflow DAGs folder
WORKDIR /usr/local/airflow/dags

# Copy your DAG file into the container
COPY dags/tips_dag.py .
RUN airflow db init

CMD ["airflow", "webserver"]