from smolagents import ToolCallingAgent, HfApiModel, DuckDuckGoSearchTool

class ContentAgent:
    def __init__(self):
        self.agent = ToolCallingAgent(
            tools=[
                DuckDuckGoSearchTool(),
            ],
            model=HfApiModel(),
            max_steps=8,
            name="content_generator",
            description="Fetch content from Duck Duck API",
        )