import streamlit as st
from _pages import (
    create_welcome_page,
    create_example_page,
    create_kafka_page,
    create_flink_page,
    create_results_page,
)

# Define pages with their corresponding functions and icons
pages = {
    "Welcome": {"fn": create_welcome_page, "icon": "👋"},
    "Example": {"fn": create_example_page, "icon": "👀"},
    "Kafka": {"fn": create_kafka_page, "icon": "🔧"},
    "Flink": {"fn": create_flink_page, "icon": "🏃"},
    "Results": {"fn": create_results_page, "icon": "📊"},
}

def main():
    st.set_page_config(
        page_title="Self-Service Streaming Pipeline App",
        menu_items={
            "Report a bug": None,
            "About": None,
        },
        layout="wide",
    )
    # Create a dictionary of page options with icons
    page_options = {f"{pages[page_name]['icon']} {page_name}": page_name for page_name in pages.keys()}

    # Create a selectbox in the sidebar for page navigation
    selected_option = st.sidebar.selectbox(
        label="Pages",
        key="page",
        options=page_options,
    )
    
    # Call the function for the selected page
    selected_page = page_options[st.session_state["page"]]
    pages[selected_page]["fn"]()

    # Debugging statement
    print(f"Selected page: {selected_page}")

if __name__ == "__main__":
    main()
