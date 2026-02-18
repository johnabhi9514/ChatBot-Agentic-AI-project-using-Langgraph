# Import Streamlit for UI
import streamlit as st

# Import message types used in LangGraph / LangChain
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage

# Import json (may be used later for formatting results)
import json

class DisplayResultsStreamlit:

    def __init__(self, usecase, graph, user_message):
        """
        Constructor:
        usecase      → selected use case (e.g., Basic Chatbot)
        graph        → compiled LangGraph graph
        user_message → message entered by user
        """
        self.usecase = usecase
        self.graph = graph
        self.user_message = user_message

    def display_result_on_ui(self):
        """
        Runs the graph and displays results in Streamlit chat UI
        """
        # Get stored values
        usecase = self.usecase
        graph = self.graph
        user_message = self.user_message

        # 1. Always display user message FIRST (outside the logic loops)
        with st.chat_message("user"):
            st.write(user_message)

        # --- Use Case: Basic Chatbot ---
        if usecase == "Basic Chatbot":
            # Stream events from LangGraph
            # Corrected input format: messages should be a list of message objects
            for event in graph.stream({"messages": [HumanMessage(content=user_message)]}):
                for value in event.values():
                    # value["messages"] is a list, we want the content of the last message
                    last_msg = value["messages"][-1]
                    
                    with st.chat_message("assistant"):
                        st.write(last_msg.content)

        # --- Use Case: Chatbot with Tool ---
        elif usecase == "Chatbot with Tool":
            # Fix: Ensure this block is indented inside display_result_on_ui
            initial_state = {"messages": [HumanMessage(content=user_message)]}
            res = graph.invoke(initial_state)

            for message in res['messages']:
                # Use isinstance() for cleaner type checking
                if isinstance(message, ToolMessage):
                    with st.chat_message("assistant"): # 'ai' role is often mapped to assistant UI
                        st.caption("🛠️ Tool Call")
                        st.code(message.content)
                
                elif isinstance(message, AIMessage) and message.content:
                    with st.chat_message("assistant"):
                        st.write(message.content)
        
        # --- AI News Execution and Display ---
        elif usecase == "AI News":
            frequency = self.user_message
            with st.spinner("Fetching and summarizing news... ⌛"):
                result = graph.invoke({"messages": frequency})
                try:
                    # Read the markdown file
                    AI_NEWS_PATH = f"./AINews/{frequency.lower()}_summary.md"
                    with open(AI_NEWS_PATH, "r") as file:
                        markdown_content = file.read()

                    # Display the markdown content in Streamlit
                    st.markdown(markdown_content, unsafe_allow_html=True)
                except FileNotFoundError:
                    st.error(f"News Not Generated or File not found: {AI_NEWS_PATH}")
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")