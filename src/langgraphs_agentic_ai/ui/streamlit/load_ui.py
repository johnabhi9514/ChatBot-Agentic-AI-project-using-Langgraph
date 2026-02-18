# Import Streamlit for building UI
import streamlit as st

# Import OS (useful if you later read environment variables, paths, etc.)
import os

# Import Config class that reads values from uiconfigfile.ini
from src.langgraphs_agentic_ai.ui.config_ui import Config


class LoadStreamlitUI:
    def __init__(self):
        """
        Constructor:
        - Loads configuration file
        - Creates a dictionary to store user selections
        """
        self.config = Config()
        self.user_controls = {}

    def load_streamlit_ui(self):
        """
        Builds the Streamlit UI:
        - Sets page title and layout
        - Creates sidebar controls
        - Stores user inputs
        """

        # Set Streamlit page configuration
        st.set_page_config(
            page_title="🤖 " + self.config.get_page_title(),
            layout="wide"
        )

        # Display page header
        st.header("🤖 " + self.config.get_page_title())

        # ✅ Initialize session state safely
        if "IsFetchButtonClicked" not in st.session_state:
            st.session_state["IsFetchButtonClicked"] = False

        if "timeframe" not in st.session_state:
            st.session_state["timeframe"] = ""

        # Sidebar section
        with st.sidebar:

            llm_options = self.config.get_llm_options()
            usecase_options = self.config.get_usecase_options()

            # LLM Selection
            self.user_controls["selected_llm"] = st.selectbox(
                "Select LLM",
                llm_options
            )

            # If Groq selected
            if self.user_controls["selected_llm"] == "Groq":

                model_options = self.config.get_groq_model_options()

                self.user_controls["selected_groq_model"] = st.selectbox(
                    "Select Model",
                    model_options
                )

                groq_key = st.text_input(
                    "GROQ API Key",
                    value=st.session_state.get("GROQ_API_KEY", ""),
                    type="password"
                )

                if groq_key:
                    st.session_state["GROQ_API_KEY"] = groq_key
                    os.environ["GROQ_API_KEY"] = groq_key
                    self.user_controls["GROQ_API_KEY"] = groq_key
                else:
                    st.warning(
                        "⚠ Please enter your GROQ API key to proceed. "
                        "Don't have one? Refer: https://console.groq.com"
                    )

            # Use Case Selection
            self.user_controls["selected_usecase"] = st.selectbox(
                "Select Usecases",
                usecase_options
            )

            # Tavily required
            if self.user_controls["selected_usecase"] in ["Chatbot with Tool", "AI News"]:

                tavily_key = st.text_input(
                    "TAVILY_API_KEY",
                    value=st.session_state.get("TAVILY_API_KEY", ""),
                    type="password"
                )

                if tavily_key:
                    st.session_state["TAVILY_API_KEY"] = tavily_key
                    os.environ["TAVILY_API_KEY"] = tavily_key
                    self.user_controls["TAVILY_API_KEY"] = tavily_key
                else:
                    st.warning(
                        "⚠ Please enter your Tavily API key to proceed. "
                        "Refer: https://app.tavily.com/home"
                    )

            # AI News UI
            if self.user_controls["selected_usecase"] == "AI News":

                st.subheader("📰 AI News Explorer")

                time_frame = st.selectbox(
                    "📅 Select Time Frame",
                    ["Daily", "Weekly", "Monthly"],
                    index=0
                )

                if st.button("🔍 Fetch Latest AI News", use_container_width=True):
                    st.session_state["IsFetchButtonClicked"] = True
                    st.session_state["timeframe"] = time_frame

        return self.user_controls
