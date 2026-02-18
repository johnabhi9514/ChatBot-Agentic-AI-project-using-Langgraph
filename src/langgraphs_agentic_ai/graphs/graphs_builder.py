from langgraph.graph import StateGraph, START, END
from src.langgraphs_agentic_ai.states.state import State
from src.langgraphs_agentic_ai.nodes.basic_chatbot_node import BasicChatbotNode
from langgraph.prebuilt import ToolNode, tools_condition
from src.langgraphs_agentic_ai.tools.search_tool import get_tools,create_tool_node
from src.langgraphs_agentic_ai.nodes.chatbot_node_with_tools import ChatbotNodeWithTool
from src.langgraphs_agentic_ai.nodes.ai_news_nodes import AINewsNode


class GraphBuilder:
    def __init__(self, model):
        self.llm = model
        self.graph_builder = StateGraph(State)

    
    def basic_chatbot_builder_graph(self):
        """
        Build a basic chatbot graph using langgraph
        this method initialized a chatbot using basic chatbot builder graph class
        and integrate it into the graph. The chatbot node is set as both entry & exit point
        of the graph
        """
        self.basic_chatbot_node = BasicChatbotNode(self.llm)
        self.graph_builder.add_node("chatbot", self.basic_chatbot_node.process)
        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_edge("chatbot", END)

    def chatbot_with_tools_build_graph(self):
        """
            Builds an advanced chatbot graph with tool integration.
            This method creates a chatbot graph that includes both a chatbot node
            and a tool node. It defines tools, initializes the chatbot with tool
            capabilities, and sets up conditional and direct edges between nodes.
            The chatbot node is set as the entry point.
        """

        ## Define the tool and tool node
        tools = get_tools()
        # tool_node is usually created using the prebuilt ToolNode
        tool_node = create_tool_node(tools)

        ## Define LLM
        llm = self.llm

        # Add chatbot nodes
        obj_chatbot_with_nodes = ChatbotNodeWithTool(llm)
        chatbot_node = obj_chatbot_with_nodes.create_chatbot(tools)
        # Replace the empty string "" with the chatbot function defined above
        self.graph_builder.add_node("chatbot", chatbot_node)
        self.graph_builder.add_node("tools", tool_node)

        # Define conditional and direct edges
        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_conditional_edges(
            "chatbot",
            tools_condition,
        )
        self.graph_builder.add_edge("tools", "chatbot")
    
    def ai_news_builder_graph(self):
        ai_news_node = AINewsNode(self.llm)

        ## added the nodes
        self.graph_builder.add_node("fetch_news",ai_news_node.fetch_news)
        self.graph_builder.add_node("summarize_news",ai_news_node.summarize_news)
        self.graph_builder.add_node("save_result",ai_news_node.save_result)

        #added the edges
        self.graph_builder.set_entry_point("fetch_news")
        self.graph_builder.add_edge("fetch_news","summarize_news")
        self.graph_builder.add_edge("summarize_news","save_result")
        self.graph_builder.add_edge("save_result", END)
    
    
    
    def setup_graph(self, usecase:str):
        """
        setup the graph base selected usecase
        """
        if usecase == "Basic Chatbot":
            self.basic_chatbot_builder_graph()
        
        if usecase == "Chatbot with Tool":
            self.chatbot_with_tools_build_graph()
        
        if usecase == "AI News":
            self.ai_news_builder_graph()
        
        return self.graph_builder.compile()