import streamlit as st

def create_flink_page():
    """
    # Write your own Flink job
    """
    python_text = "# Your Flink job code goes here\n\n"
    pyflink_text = st.text_area(
        label="Write/edit the query below",
        key="xyz",
        value=python_text,
        height=400,
    )
    if st.button("Run Job"):
        # Here you can run the Flink job using pyflink_text
        # For demonstration purposes, let's just display the job code
        st.write("Running Flink job with the following code:")
        st.code(pyflink_text, language="python")
        

if __name__ == "__main__":
    create_flink_page()
