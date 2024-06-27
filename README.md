# Self-Service App for Building a Streaming Pipeline with Kafka and Flink

## Running this project

You can run this project locally or in Docker. 

**Important considerations**:
- Kafka and Flink are preinstalled if using Docker. However, this is not the case if running locally, unless you have Kafka and Flink installed on your local machine.
- The Streamlit app will not update automatically if running in Docker so you will need to manually run `make restart` to refresh the app.

### On local machine

You have two options to run this project locally:

**Option 1: Using Make**

- Simply run: 
    ```bash
    make run local
    ```

**Option 2: Manually**

1. Create a virtual environment
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

2. Install python packages
    ```bash
    pip install -r requirements-streamlit.txt
    ```

3. Run streamlit app
    ```bash
    streamlit run streamlit_app.py 
    ```

### Using Docker
- Run **`make run docker`**


## Tips
- Edit the Streamlit pages by modifying files in `_pages`
- Modify the navbar in `streamlit_app.py` 
- Run `make help` to see all available `make` commands

## References
- [Streamlit Cheat Sheet](https://docs.streamlit.io/develop/quick-reference/cheat-sheet)
- [Streamlit API Reference](https://docs.streamlit.io/develop/api-reference)


License
----------

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
