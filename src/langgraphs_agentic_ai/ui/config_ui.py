# Import ConfigParser to read values from .ini configuration files
from configparser import ConfigParser


class Config:
    def __init__(self, config_file="./src/langgraphs_agentic_ai/ui/config_ui.ini"):
        """
        Constructor:
        - Creates a ConfigParser object
        - Reads the given .ini configuration file
        """

        # Create parser object
        self.config = ConfigParser()

        # Read configuration file
        self.config.read(config_file)

    def get_llm_options(self):
        """
        Returns available LLM options from config file.
        Example output: ['Groq']
        """
        return self.config["DEFAULT"].get("LLM_OPTIONS").split(", ")

    def get_usecase_options(self):
        """
        Returns available use-case options.
        Example output: ['Basic Chatbot']
        """
        return self.config["DEFAULT"].get("USECASE_OPTIONS").split(", ")

    def get_groq_model_options(self):
        """
        Returns available Groq model options.
        Example output:
        ['llama3-8b-8192', 'llama3-70b-8192', 'gemma2-9b-it']
        """
        return self.config["DEFAULT"].get("GROQ_MODEL_OPTIONS").split(", ")

    def get_page_title(self):
        """
        Returns the page title from config file.
        """
        return self.config["DEFAULT"].get("PAGE_TITLE")
