# Self-Service App for Building a Streaming Pipeline with Kafka and Flink

## Running this project

### Steps:
- Install Docker Desktop.
- Open Docker so it's running in the background.
- Run **`make run`** to start the application.

### Considerations:
- Kafka and Flink are preinstalled in the Docker container.
- The Streamlit app will not update automatically if running in Docker so you will need to manually run `make restart` to refresh the app.

### Tips
- Edit the Streamlit pages by modifying files in `_pages`
- Modify the navbar in `streamlit_app.py` 
- Run `make help` to see all available `make` commands

### References
- [Streamlit Cheat Sheet](https://docs.streamlit.io/develop/quick-reference/cheat-sheet)
- [Streamlit API Reference](https://docs.streamlit.io/develop/api-reference)


License
----------

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
