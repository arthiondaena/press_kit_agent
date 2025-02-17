from smolagents import CodeAgent, HfApiModel

class ReviewAgent:
    def __init__(self):
        self.agent = CodeAgent(
            tools=[],
            model=HfApiModel(),
            name="quality_reviewer",
            description="Evaluates press kit quality and provides feedback"
        )