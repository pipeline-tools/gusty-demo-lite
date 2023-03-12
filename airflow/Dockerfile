FROM python:3.9.1-slim-buster
USER root

# Postgres Requirements (For our Metadata Database)
RUN apt-get update && apt-get install -y libpq-dev build-essential
RUN pip3 install psycopg2

# Install airflow and gusty
RUN pip3 install apache-airflow==2.5.1
RUN pip3 install gusty==0.18.0

# Airflow Env Vars
ENV AIRFLOW_HOME='/usr/local/airflow'

# Set wd
WORKDIR /usr/local/airflow

# Sleep forever
# CMD sleep infinity
