import streamlit as st

def create_kafka_page():
    """
    # Create your own Kafka topic
    """
    st.header("Create your own Kafka topic!")
    st.info("""
    ### Confluent cloud setup
    Confluent cloud provides a free 30 days trial for, you can signup [here](https://www.confluent.io/confluent-cloud/tryfree/)
    """)


if __name__ == "__main__":
    create_kafka_page()