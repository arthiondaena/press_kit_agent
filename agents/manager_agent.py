from smolagents import CodeAgent, HfApiModel, UserInputTool, tool
from .content_agent import ContentAgent
from .review_agent import ReviewAgent

@tool
def write_file(file_name: str, content: str) -> None:
    """Write content to a file
    Args:
        file_name: file name
        content: content to write
    """
    with open(file_name, 'w') as f:
        f.write(content)

@tool
def read_file(file_name: str) -> str:
    """Read a file
    Args:
        file_name: file name
    """
    with open(file_name, 'r') as f:
        return f.read()

@tool
def read_md_file(file_path: str) -> str:
    """Read a Markdown file
        Args:
            file_path: file path of the markdown file
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

@tool
def preview_content(content: str) -> None:
    """Print the content to the console. Don't pass markdown formatting.
        Args:
            content: content to print"""
    print(content)


class ManagerAgent:
    def __init__(self):
        self.model = HfApiModel()
        self.content_agent = ContentAgent()
        self.review_agent = ReviewAgent()

        self.agent = CodeAgent(
            tools=[UserInputTool(), preview_content
                # , write_file, read_file, read_md_file
                   ],
            model=self.model,
            managed_agents=[self.content_agent.agent, self.review_agent.agent],
            additional_authorized_imports=["datetime", "json", "file", "mdutils"],
            max_steps = 50
        )