import os
import json
import requests
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.table import EnvironmentSettings, DataTypes, StreamTableEnvironment
from pyflink.table.udf import ScalarFunction, udf


def create_kafka_sink(t_env):
    table_name = "process_events_kafka"
    sink_ddl = f"""
        CREATE TABLE {table_name} (
            <table definition>
        ) WITH (
            'connector' = 'kafka',
            'properties.bootstrap.servers' = '{os.environ.get('KAFKA_URL')}',
            'topic' = '{os.environ.get('KAFKA_GROUP').split('.')[0] + '.' + table_name}'
        );
        """
    t_env.execute_sql(sink_ddl)
    return table_name


def create_postgres_sink(t_env):
    table_name = "processed_events"
    sink_ddl = f"""
        CREATE TABLE {table_name} (
            <table definition>
        ) WITH (
            'connector' = 'jdbc',
            'url' = 'jdbc:postgresql://postgres:5632/postgres',
            'table-name' = '{table_name}',
            'username' = 'postgres',
            'password' = 'postgres',
            'driver' = 'org.postgresql.Driver'
        );
        """
    t_env.execute_sql(sink_ddl)
    return table_name


def create_kafka_source(t_env):
    table_name = "events"
    pattern = "yyyy-MM-dd''T''HH:mm:ss.SSS''Z''"
    source_ddl = f"""
        CREATE TABLE {table_name} (
            <table definition>
        ) WITH (
            'connector' = 'kafka',
            'properties.bootstrap.servers' = '{os.environ.get('KAFKA_URL')}',
            'topic' = '{os.environ.get('KAFKA_TOPIC')}'
        );
        """
    t_env.execute_sql(source_ddl)
    return table_name


def log_processing():
  # Set up the execution environment
  env = StreamExecutionEnvironment.get_execution_environment()
  # env.set_parallelism(1)

  # Set up the table environment
  settings = EnvironmentSettings.new_instance().in_streaming_mode().build()
  t_env = StreamTableEnvironment.create(env, environment_settings=settings)

  try:
    # Create Kafka table
    source_table = create_kafka_source(t_env)
    kafka_sink = create_kafka_sink(t_env)
    postgres_sink = create_postgres_sink(t_env)

    t_env.execute_sql(
      f"""
      INSERT INTO {kafka_sink}
      SELECT *
      FROM {source_table}
      """
    )

    # write records to postgres too!
    t_env.execute_sql(
      f"""
        INSERT INTO {postgres_sink}
        SELECT *
        FROM {source_table}
        """
    ).wait()

  except Exception as e:
    print("Writing records from Kafka to JDBC failed:", str(e))


if __name__ == "__main__":
    log_processing()
