from src.langgraphs_agentic_ai.graphs.graphs_builder import GraphBuilder
import streamlit as st
from src.langgraphs_agentic_ai.ui.streamlit.load_ui import LoadStreamlitUI
from src.langgraphs_agentic_ai.llms.groqllm import GroqLLM
from src.langgraphs_agentic_ai.ui.streamlit.display_result import DisplayResultsStreamlit


def init_session_state():
    """
    Initialize all required session state variables.
    This MUST run before accessing them anywhere.
    """
    defaults = {
        "IsFetchButtonClicked": False,
        "timeframe": "",
        "GROQ_API_KEY": "",
        "TAVILY_API_KEY": ""
    }

    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def load_langgraph_agentic_app():

    # ✅ Initialize session state FIRST
    init_session_state()

    # ---------------------------
    # Load UI
    # ---------------------------
    ui = LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()

    if not user_input:
        st.error("Error: Failed to load user input from UI")
        return

    # ---------------------------
    # Chat input logic (SAFE ACCESS)
    # ---------------------------
    if st.session_state.get("IsFetchButtonClicked", False):
        user_message = st.session_state.get("timeframe", "")
        # Reset button after use (important!)
        st.session_state["IsFetchButtonClicked"] = False
    else:
        user_message = st.chat_input("Please enter your message")

    # ---------------------------
    # Run only when user submits message
    # ---------------------------
    if user_message:
        try:

            obj_llm_config = GroqLLM(user_controls_input=user_input)
            model = obj_llm_config.get_llm_model()

            if not model:
                st.error("Error: LLM model can't be initialized")
                return

            usecase = user_input.get("selected_usecase")

            if not usecase:
                st.error("Error: No usecase selected")
                return

            graph_builder = GraphBuilder(model)

            try:
                graph = graph_builder.setup_graph(usecase)

                if not graph:
                    st.error("Error: Graph was not created")
                    return

                DisplayResultsStreamlit(
                    usecase, graph, user_message
                ).display_result_on_ui()

            except Exception as graph_error:
                st.error(f"Error: Graph setup failed - {graph_error}")
                return

        except Exception as e:
            st.error(f"Unexpected error occurred: {e}")
